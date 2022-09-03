from peewee import PostgresqlDatabase

# Connect to a Postgres database.
def create_db():
  return PostgresqlDatabase('greg', user='postgres', password='asdfasdf',
                           host='db', port=5432)

# simple utility function to create tables
def create_tables():
    from models import Log
    db = create_db()
    with db:
        db.create_tables([Log])