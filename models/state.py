#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
import os

class State(BaseModel, Base):
    __tablename__ = 'states'
        """ State class """
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="States", cascade="all, delete")
    else:
        @property
        def cities(self):
        """
         Getter attribute that returns the list of City instances
        with state_id equals to the current State.id
        """
        from models import Storage, City
        cityList == []
        for city in storage.all(city).values():
            if city.state_id == self.id
                cityList.append(city)
        return cityList
        
