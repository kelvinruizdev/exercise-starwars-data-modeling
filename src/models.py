import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    favorites = relationship("Favorite", back_populates="user")

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    climate = Column(String(50), nullable=False)
    terrain = Column(String(50), nullable=False)
    population = Column(Integer, nullable=False)

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    gender = Column(String(20), nullable=False)
    birth_year = Column(String(50), nullable=False)
    skin_color = Column(String(50), nullable=False)

class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="favorites")
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship("Planet")
    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship("Character")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
