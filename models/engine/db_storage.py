#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
#from models.user import User
from models.city import City
from models.state import State
#from models.amenity import Amenity
#from models.place import Place
#from models.review import Review

import os
class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                       .format(os.environ.get("HBNB_MYSQL_USER"),
                                               os.environ.get('HBNB_MYSQL_PWD'),
                                               os.environ.get('HBNB_MYSQL_HOST'),
                                               os.environ.get('HBNB_MYSQL_DB')),
                                        pool_pre_ping=True)

    if os.environ.get('HBNB_ENV') == 'test':
       Base.metadata.drop_all('self.__engine')

    def all(self, cls=None):
        if cls:
            results = self.__session.query(eval(cls).all())
        else:
             results = self.__session.query(State).all()
             results.extend(self.__session.query(State).all())
        return {f"{obj.__class__.__name__}.{obj.id}": obj for obj in results}

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj != None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
