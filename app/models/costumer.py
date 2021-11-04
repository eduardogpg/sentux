import uuid

from . import db
from peewee import *

from datetime import datetime

class Costumer(Model):
    email = CharField(null=False, max_length=255, unique=True)
    uuid = CharField(null=False, max_length=255)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db
        table_name = 'costumers'

    @property
    def wallet(self):
        if self.wallets:
            return self.wallets[0]

def create_costumer(email):
    try:
        costumer = Costumer.create(
            email=email,
            uuid=uuid.uuid4().hex
        )

        return costumer
    
    except Exception as err:
        print(err)
        return None