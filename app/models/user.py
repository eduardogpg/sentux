from . import db
from peewee import *

from datetime import datetime

class User(Model):
    username = CharField(null=False, max_length=255)
    email = CharField(null=False, max_length=255)

    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db
        table_name = 'users'