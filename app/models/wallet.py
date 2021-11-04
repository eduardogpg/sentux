import json
from . import db
from peewee import *

from enum import Enum

from datetime import datetime

from .costumer import Costumer

from hdwallet import HDWallet
from hdwallet.symbols import BTC

MNEMONIC = "boy again trick style uphold law panther agent dial inner dolphin flush"
SEED = "3a24860bb5115915fe866b7d5c288192d00071339701c8716a4966e0a937ad1edda7097b72438a4c35a962fd634c1a32a2ffdb853e7f65b80b401a49d6462dbf"

class Criptocurrency(Enum):
    BITCOIN = 0

class Wallet(Model):
    address = CharField(max_length=255, null=False)
    costumer = ForeignKeyField(Costumer, related_name='wallets')
    criptocurrency = IntegerField(null=False, default=Criptocurrency.BITCOIN)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db
        table_name = 'wallets'


def create_hd_wallet(identifier):
    hdwallet: HDWallet = HDWallet(symbol=BTC)
    hdwallet.from_seed(SEED)

    hdwallet.from_index(44, hardened=True) # purpose
    hdwallet.from_index(0, hardened=True) # coin_type = BTC
    hdwallet.from_index(identifier, hardened=True) # account
    hdwallet.from_index(0) # change 0 = Wallets para recibir dinero
    hdwallet.from_index(0) # address_index

    return hdwallet

def create_wallet(costumer):
    hdwallet = create_hd_wallet(costumer.id)
    address = hdwallet.dumps()['addresses']['p2pkh']

    wallet = Wallet.create(address=address, costumer=costumer)
    return wallet