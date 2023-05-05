#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey

class City(BaseModel Base):
    """ The city class, contains state ID and name """
    __tablename__
    state_id = Column(string(60), nullable=False)
    name = Column(string(128), nullable=False)
 
