from app import create_app
from app.models.criptocurrency import get_current_crypto_price, convert

# app = create_app()

print(
    convert(200, 'bitcoin')
)
