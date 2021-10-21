from fastapi import FastAPI

from .v1 import v1 as v1_routers

def create_app():
    app = FastAPI()
    
    app.include_router(v1_routers)

    return app