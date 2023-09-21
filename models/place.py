#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, Integer, Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import os
import models
from models.amenity import Amenity
from models.review import Review


associationTable = Table('place_amenity', Base.metadata,
                         Column('place_id', String(60),
                                ForeignKey('places.id'), primary_key=True,
                                nullable=False),
                         Column('amenity_id', String(60),
                                ForeignKey('amenities.id'), primary_key=True,
                                nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(128), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(128), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(128), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan')
        amenities = relationship('Amenity', secondary=associationTable,
                                 backref='place_amenities')
        amenity_ids = []


    @property
    def reviews(self):
        """
        Get reviews and build a list
        """
        from models import storage
        reviewsList = []
        data = storage.all(Review)
        for review in data.values():
            if review.place_id == self.id:
                reviewsList.append(review)
            return reviewsList

    @property
    def amenities(self):
        """
        Get amenities
        """
        from models import storage
        amenities = []
        data = storage.all(Amenity)
        for amenity in data.values():
            amenities.append(amenity)
        return amenities

    @amenities.setter
    def amenities(self,obj):
        """
        Setter for amenities
        """
        if isinstance(obj, Amenity):
            self.amenity_ids.append(obj.id)
