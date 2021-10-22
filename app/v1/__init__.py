from fastapi import APIRouter

from .invoice import invoices as invoices_routers
from .costumer import costumers as costumers_routers

v1 = APIRouter(prefix='/v1')

v1.include_router(invoices_routers)
v1.include_router(costumers_routers)