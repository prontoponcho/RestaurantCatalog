__all__ = ["restaurant", "menu", "api", "static"]

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from catalog.models.database_setup import Base

engine = create_engine('sqlite:///./catalog/models/restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
