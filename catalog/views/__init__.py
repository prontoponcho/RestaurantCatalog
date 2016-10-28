__all__ = ["restaurant", "menu", "api", "static", "login", "user"]

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from catalog.models.database_setup import Base

engine = create_engine('postgres://yyxwqovxkfifbc:7rQPBXfpX7RdhhzcFwtWaAOBv8@ec2-54-243-249-176.compute-1.amazonaws.com:5432/dffbvi3bmqmjca')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
