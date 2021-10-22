from . import db
from peewee import *

from datetime import datetime

class Wallet(Model):
    costumer = ForeignKeyField(Costumer, related_name='wallets')
    criptocurrency = CharField(max_length=255, null=False, default='BTC')
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db
        table_name = 'wallets'


def create_wallet(costumer):
