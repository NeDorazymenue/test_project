from pydantic import BaseModel
from datetime import datetime

class Transaction(BaseModel):
    transaction_id: str
    user_id: int
    account_id: int
    amount: float
    created_at: datetime