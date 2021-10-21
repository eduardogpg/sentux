from fastapi import APIRouter

costumers = APIRouter(prefix='/costumers')

@costumers.get('/')
async def ping():
    return {'mensaje': 'Hola mundo'}