#!/usr/bin/python3
"""
Imported modules
os
sqlalchemy
"""
from sqlalchemy import create_engine, Column, String, MetaData
from sqlalchemy.orm import sessionmaker, relationship, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import os
from os import getenv
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.user import User
from models.state import State
from models.review import Review


class DBStorage:
    """
    create link between app and mysql via MYSQLAlchemy
    Params:
     _engine: private class attribute-specify db engine
     _session: ''     ''     ''  - create/start session
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Creates the engine and links to hbnb_dev and hbnb_dev_db:
        hbnb_dev - db and hbnb_dev_db - user
        """
        # Retrieving MySQL connection details from environment variables
        mysqlUser = os.getenv('HBNB_MYSQL_USER')
        mysqlPwd = os.getenv('HBNB_MYSQL_PWD')
        mysqlHost = os.getenv('HBNB_MYSQL_HOST')
        mysqlDb = os.getenv('HBNB_MYSQL_DB')

        dbUrl = f'mysql+mysqldb://{mysqlUser}:{mysqlPwd}@{mysqlHost}/{mysqlDb}'

        self.__engine = create_engine(dbUrl, pool_pre_ping=True)
        if getenv('HBNB_ENV ') == 'test':
            # Drop all tables if in test environment
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query all objects depending on the class name (arg cls)
        if cls is None,query all type of objects;
           Return a dict of queried objects in format
             key = <class-name>.<object-id>
        """
        if cls is None:
            obj = self.__session.query(State).all()
            obj.extend(self.__session.query(User).all())
            obj.extend(self.__session.query(City).all())
            obj.extend(self.__session.query(Amenity).all())
            obj.extend(self.__session.query(Place).all())
            obj.extend(self.__session.query(Review).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            obj = self.__session.query(cls)
        return {f"{type(i).__name__}.{i.id}":i for i in obj}

    def new(self, obj):
        """
        Adds the obj to the current db session
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all the changes of the current db session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete from the current db session obj if not none
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database
        Create the current database session
        """
        Base.metadata.create_all(self.__engine)
        newSesh = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(newSesh)
        self.__session = Session()

    def close(self):
        """
        Close the current SQLAlchemy session
        """
        self.__session.remove()
