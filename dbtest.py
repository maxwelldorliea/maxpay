from models import engine
from sqlalchemy import text

with engine.connect() as conn:
    res = conn.execute(text("select 'hello word'"))
    print(res.all())
