from peewee import *

from local_settings import DATABASE_USER
from local_settings import DATABASE_PASSWORD

db = MySQLDatabase('sentuxproject',
                user=DATABASE_USER,
                password=DATABASE_PASSWORD,
                host='localhost',
                port=3306)