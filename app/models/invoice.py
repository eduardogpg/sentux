import uuid

from . import db
from peewee import *

from datetime import datetime

from .costumer import Costumer

class Invoice(Model):
    costumer = ForeignKeyField(Costumer, related_name='invoices')
    price = FloatField(null=False, default=0.0)    
    # Aquí viene el precio en Criptos?
    uuid = CharField(null=False, max_length=255)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db
        table_name = 'invoices'


def create_invoice(costumer_uuid, price):
    try:
        with db.atomic() as transaction:
            costumer = Coustumer.select().where(uuid==costumer_uuid).first()
            if costumer:

                invoce = Invoice.create(costumer=costumer, price=price)
                
            else:
                return None

    except Exception as err:
        print(err)
        return None
