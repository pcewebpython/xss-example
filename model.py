""" script model.py """

# imports
import os

from peewee import Model, CharField
from playhouse.db_url import connect

# database connect
DB = connect(os.environ.get('DATABASE_URL', 'sqlite:///my_database.db'))


class Message(Model):
    """ mesage class """
    content = CharField(max_length=1024, unique=True)

    class Meta:
        """ mata class """
        database = DB
