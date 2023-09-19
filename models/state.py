#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, ForeignKey
from sqlalchemy import Column
from sqlalchemy import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
