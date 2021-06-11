import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///static/data/octo.db', echo=True)
conn = engine.connect()
meta = sqlalchemy.MetaData()