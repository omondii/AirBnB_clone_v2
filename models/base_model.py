#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Interger, Datetime

Base = declarative_base()
class BaseModel:
    """
    A base class for all hbnb models
    Paramas: sqlalchemy class attributes
      id: a column containing a unique string (60 characters)
      created_at: a column containing a datetime
      updated_at: a column containing a datetime
    """

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(Datetime, nullable=False, default=datetime.utcnow())
    updated_at = Column(Datetime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if kwargs.get("updated_at") or (kwargs.get("created_at")):
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            if kwargs.get("__class__"):
                del kwargs['__class__']
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary.pop("_sa_instance_state", None)
        return dictionary

    def delete(self):
        """ Deletes the current instnce from storage """
        models.storage.delete(self)
