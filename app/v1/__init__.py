from fastapi import APIRouter

from .costumer import costumers as costumers_routers

v1 = APIRouter(prefix='/v1')

v1.include_router(costumers_routers)