import hashlib
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from fastapi import HTTPException
from src.models.accounts import AccountsOrm
from src.models.users import UsersOrm
from src.models.transactions import TransactionsOrm
from src.config import settings
from src.api.dependencies import DBDep


import hashlib

transaction_id = "5eae174f-7cg0-472c-bd36-35660f00132b"
user_id = 2
account_id = 1
amount = 200.0
secret_key = "gfdmhghif38yrf9ew0jkf32"


def create_signature(transaction_id, user_id, account_id, amount, secret_key):
    data = f"{str(transaction_id)}{str(user_id)}{str(account_id)}{str(amount)}{secret_key}"
    return hashlib.sha256(data.encode()).hexdigest()

generated_signature = create_signature(transaction_id, user_id, account_id, amount, secret_key)
print(f"Generated signature: {generated_signature}")


def validate_signature(data: dict, secret_key: str) -> bool:
    raw_string = f"{str(data['transaction_id'])}{str(data['user_id'])}{str(data['account_id'])}{str(data['amount'])}{secret_key}"
    signature = hashlib.sha256(raw_string.encode()).hexdigest()
    return signature == data['signature']


async def process_webhook_data(webhook_data, db: DBDep):
    if not validate_signature(webhook_data.dict(), secret_key):
        raise HTTPException(status_code=400, detail="Invalid signature")
    result = await db.session.execute(select(TransactionsOrm).filter_by(transaction_id=webhook_data.transaction_id))
    if result.scalars().first():
        raise HTTPException(status_code=400, detail="Transaction already processed")
    result = await db.session.execute(
        select(UsersOrm).filter_by(id=webhook_data.user_id).options(selectinload(UsersOrm.accounts))
    )
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    account = next((acc for acc in user.accounts if acc.id == webhook_data.account_id), None)

    if not account:
        account = AccountsOrm(user_id=webhook_data.user_id, balance=0)
        db.session.add(account)
        await db.commit()

    new_transaction = TransactionsOrm(
        transaction_id=webhook_data.transaction_id,
        user_id=webhook_data.user_id,
        account_id=webhook_data.account_id,
        amount=webhook_data.amount,
    )
    db.session.add(new_transaction)
    await db.commit()

    if webhook_data.amount > 0:
        account.balance += webhook_data.amount
    elif webhook_data.amount < 0:
        if account.balance + webhook_data.amount < 0:
            raise HTTPException(status_code=400, detail="Insufficient funds")
        account.balance += webhook_data.amount

    await db.commit()