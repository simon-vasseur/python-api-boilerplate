from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine("sqlite:///app.db")

SessionMaker = sessionmaker(bind=engine)
session = SessionMaker()
