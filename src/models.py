import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True, nullable=False)
    climate = Column(String(50), nullable=False)
    terrain = Column(String(50), nullable=False)
    population = Column(Integer, nullable=False)
    create_at = Column(DateTime(timezone=False))
    update_at = Column(DateTime(timezone=False)) 
    favorite = relationship('Favorite', back_populates='planets')  

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True, nullable=False)
    gender = Column(String(20), nullable=False)
    birth_year = Column(String(50), nullable=False)
    skin_color = Column(String(50), nullable=False)
    create_at = Column(DateTime(timezone=False))
    update_at = Column(DateTime(timezone=False))
    favorite = relationship('Favorite', back_populates='characters')
    

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    create_at = Column(DateTime(timezone=False))
    update_at = Column(DateTime(timezone=False))
    favorite = relationship('Favorite',back_populates='users', uselist=False)
    
class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    user = relationship('User', back_populates='favorites')
    character = relationship('Character',back_populates='favorites', uselist=True)
    planet = relationship('Planet',back_populates='favorites', uselist=True)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
