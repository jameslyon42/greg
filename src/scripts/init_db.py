from database import create_db
from models import Log

db = create_db()
with db:
    db.create_tables([Log])
