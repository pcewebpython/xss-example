""" script setup.py """

from model import DB, Message 

DB.connect()
DB.create_tables([Message])
