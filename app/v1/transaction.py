from fastapi import APIRouter
from fastapi import HTTPException

# --- Modelos para validar
from .models import CreateTransaction
from .models import RetrieveTransaction

transactions = APIRouter(prefix='/transactions')

@transactions.post('/', response_model=RetrieveTransaction)
async def create(invoice: CreateTransaction):
    costumer = Costumer.select().where(Costumer.uuid == invoice.customer_uuid).first()

    if costumer:
        if costumer.wallet is None:
            create_wallet(costumer)

        wallet = costumer.wallet
        
    raise HTTPException(status_code=404, detail="Costumer not found")