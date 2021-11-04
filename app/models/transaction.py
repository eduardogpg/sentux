import uuid

from enum import Enum

from . import db
from peewee import *

from datetime import datetime

from .wallet import Wallet
from .costumer import Costumer

class State(Enum):
    CREATED = 0
    IN_PROGRESS = 1
    FAILED = 2
    COMPLETED = 3

class Transaction(Model):
    costumer = ForeignKeyField(Costumer, related_name='transactions')
    wallet = ForeignKeyField(Wallet, related_name='transactions')
    uuid = CharField(null=False, max_length=255)
    amount = FloatField(null=False, default=0.0) 
    total = FloatField(null=False, default=0.0)
    state = IntegerField(null=False, default=0)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db
        table_name = 'transactions'



def create_transaction(costumer, wallet, amount):
   pass