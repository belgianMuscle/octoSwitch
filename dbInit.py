import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///octo.db', echo=True)
conn = engine.connect()
meta = sqlalchemy.MetaData()