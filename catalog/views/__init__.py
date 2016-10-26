__all__ = ["restaurant", "menu", "api", "static", "login", "user"]

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from catalog.models.database_setup import Base

engine = create_engine('sqlite:///./catalog/models/restaurantmenuwithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
