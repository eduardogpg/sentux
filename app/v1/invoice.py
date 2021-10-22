from fastapi import APIRouter

# --- Modelos para validar
from .models import CreateInvoice
from .models import RetrieveInvoice

invoices = APIRouter(prefix='/invoices')

@invoices.post('/', response_model=RetrieveInvoice)
async def create(invoice: CreateInvoice):
    return {}