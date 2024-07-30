#!/usr/bin/python3

import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://' + os.getenv('HBNB_MYSQL_USER') + ':' + os.getenv('HBNB_MYSQL_PWD') + '@' + os.getenv('HBNB_MYSQL_HOST') + '/' + os.getenv('HBNB_MYSQL_DB'), pool_pre_ping=True))
        self.__session = sessionmaker(bind=self.__engine)
        meta = MetaData()
        if os.getenv('HBNB_ENV') == 'Test':
            meta.drop_all(self.__engine)

    def all(self, cls=None):
        if cls == None:
            my_res = self.__session.query(User, State, City, Amenity, Place, Review)
        else:
            my_res = self.__session.query(cls)
        return my_res

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()


    def delete(self, obj=None):
        if obj != None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        ses_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(ses_factory)
