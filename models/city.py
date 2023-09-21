#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import os

class City(BaseModel, Base):
    """
    The city class, contains state ID and name
    Params:
      __tablename__ - class attribute reping the table name
      name - column containing a string (128 characters)
      state_id - column containing a string (60 characters).
    """
    __tablename__ = 'cities'
    if os.environ.get("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

        state = relationship('State', )#backref='cities')
        places = relationship('Place', backref='cities',
                              cascade='all, delete, delete-orphan')
        # amenities = relationship('Amenity', secondary=associationTable,
        # back_populates='place_amenities')
