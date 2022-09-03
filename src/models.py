from peewee import *
from database import create_db

db = create_db()

class BaseModel(Model):
    class Meta:
        database = db

class Log(BaseModel):
    content = TextField()

# simple utility function to create tables
def create_tables():
    with db:
        db.create_tables([Log])

