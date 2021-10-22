from fastapi import FastAPI

from .v1 import v1 as v1_routers

from .models import db
from .models.costumer import Costumer

def create_app():
    app = FastAPI()
    
    app.include_router(v1_routers)

    db.create_tables([Costumer])
    
    return app