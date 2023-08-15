import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    password = Column(String(20), nullable=False)
    name = Column(String(250), nullable=False)
    email = Column(String(50), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True, nullable=False)
    char_id = Column(Integer, nullable=False)
    planet_id = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    users = relationship(Users)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True, nullable=False)
    uid = Column(Integer, ForeignKey('favorites.char_id'), nullable=False)
    favorites = relationship(Favorites)
    name = Column(String(50), nullable=False)
    url = Column(String(100), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True, nullable=False)
    uid = Column(Integer, ForeignKey('favorites.planet_id'), nullable=False)
    favorites = relationship(Favorites)
    name = Column(String(50), nullable=False)
    url = Column(String(100), nullable=False)

class CharProperties(Base):
    __tablename__ = 'charProperties'
    url = Column(String(100), ForeignKey('characters.url'), primary_key=True, nullable=False)
    characters = relationship(Characters)
    homeworld = Column(String(100), nullable=False)
    height = Column(Integer, nullable=False)

class PlanetProperties(Base):
    __tablename__ = 'planetProperties'
    url = Column(String(100), ForeignKey('planets.url'), primary_key=True, nullable=False)
    planets = relationship(Planets)
    diameter = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
