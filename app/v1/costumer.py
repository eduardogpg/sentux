from fastapi import APIRouter

# --- Modelos para validar
from .models import CreateCostumer
from .models import RetrieveCostumer

# --- Modelos de la base de datos
from ..models.costumer import create_costumer

costumers = APIRouter(prefix='/costumers')

@costumers.post('/', response_model=RetrieveCostumer)
async def create(costumer: CreateCostumer):
    costumer = create_costumer(costumer.email)

    return costumer