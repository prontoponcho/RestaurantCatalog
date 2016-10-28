from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# Configuration
Base = declarative_base()

class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

# Python Classes for DB Tables
class Restaurant(Base):

    # DB Table
    __tablename__ = 'restaurant'

    # Mapper
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    category = Column(String(20), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    menuItems = relationship('MenuItem', cascade='all, delete-orphan')

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category
        }


class MenuItem(Base):

    # DB Table
    __tablename__ = 'menu_item'

    # Mapper
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'course': self.course,
        }

# Configuration
engine = create_engine('postgres://yyxwqovxkfifbc:7rQPBXfpX7RdhhzcFwtWaAOBv8@ec2-54-243-249-176.compute-1.amazonaws.com:5432/dffbvi3bmqmjca')
Base.metadata.create_all(engine)
