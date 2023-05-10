#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models.engine.file_storage import FileStorage
from models.review import Review
import os



class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True, default='NULL')
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True, default=0)
    longitude = Column(Float, nullable=True, default=0)
    amenity_ids = []

    # switching storage
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    #creating relationship
        reviews = relationship('Review', cascade= 'all, delete', backref='place')

    else:
        @property
        def reviews(self):
            reviews = []
            for review in storage.all(Review).values():
                if reviews.places_id == self.id:
                    reviews.append(review) 
            return reviews
