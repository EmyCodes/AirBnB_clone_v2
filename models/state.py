#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column,ForiegnKey,
import os

class State(BaseModel Base):
    """ State class """
    name = Column(string(128), nullable=False)
     
