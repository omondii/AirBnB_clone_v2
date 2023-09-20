#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes
    Params:
      __tablename__ class attr reping users table
      email - column containing a string (128 characters)
      password - column containing a string (128 characters)
      first_name - column containing a string (128 characters)
      last_name - column containing a string (128 characters)
    """

    __tablename__ = 'users'

    email = Column(String(128), nullable=True)
    password = Column(String(128), nullable=True)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship('Place', cascade='delete', back_populates='user')
