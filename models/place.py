#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
import gc
import os

place_amenity = Table('association', Base.metadata,
    Column('place_id', String(60), ForeignKey(place,id), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey(amenities.id), primary_key=True, nullable=False)
)

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), nullable=False, ForeignKey("cities.id"))
    user_id = Column(String(60), nullable=False, ForeignKey("users.id"))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []
    user = relationship("User", back_populates="places")
    cities = relationship("City", back_populates="places")

    if os.getenv("hbtn") == "bla":
        reviews = relationship("Review", back_populates="places")
        amenities = relationship("Amenity", secondary=place_amenity, back_populates="place_amenities", viewonly=False)
    else:
        @property
        def reviews(self):
            myobjlist = []
            myobjs = gc.get_objects()
            for ob in myobjs:
                if isinstance(ob, Review):
                    if ob.place_id == self.city_id:
                        myobjlist.append(ob)
            return myobjlist

        @property
        def amenities(self):
            myAmenList = []
            for obj in gc.get_objects():
                if isinstance(obj, Amenity):
                    if odj.id == self.amenity_id:
                        myAmenList.append(obj)
            return myAmenList

        @amenities.setter
        def amenities(self, obj):
            if isinstance(obj, Amenity):
                self.amenity_id = odj.id
