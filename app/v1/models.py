from typing import Any
from typing import Optional

from peewee import ModelSelect

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

from pydantic.utils import GetterDict

class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, ModelSelect):
            return list(res)
        return res

class CreateCostumer(BaseModel):
    email: str


class RetrieveCostumer(BaseModel):
    uuid: str

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


# ------- Transactions -------

class CreateTransaction(BaseModel):
    customer_uuid: str
    amount: float


class RetrieveTransaction(BaseModel):
    amount: float

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


