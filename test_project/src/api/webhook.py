from fastapi import APIRouter, HTTPException
from src.api.dependencies import DBDep
from src.schemas.webhook import WebhookData
from src.services.webhook import process_webhook_data
import logging

router = APIRouter(prefix="/webhook", tags=["webhook"])



@router.post("")
async def webhook(webhook_data: WebhookData, db: DBDep):
    try:
        logging.info(f"Received webhook data: {webhook_data}")
        await process_webhook_data(webhook_data, db)
        return {"status": "success", "message": "Transaction processed successfully"}
    except Exception as e:
        logging.error(f"Error processing webhook data: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Error processing webhook: {str(e)}")