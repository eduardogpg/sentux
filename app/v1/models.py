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
    email: str
    uuid: str

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class CreateInvoice(BaseModel):
    price: float = Field(..., gt=0)

