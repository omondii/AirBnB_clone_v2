#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String

class City(BaseModel, Base):
    """
    The city class, contains state ID and name
    Params:
      __tablename__ - class attribute reping the table name
      name - column containing a string (128 characters)
      state_id - column containing a string (60 characters).
    """
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False, ForeignKey("states.id"))
