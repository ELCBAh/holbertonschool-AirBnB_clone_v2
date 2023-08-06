#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Float, Integer
from sqlalchemy import Column, Table
from sqlalchemy import ForeignKey
from os import getenv
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    review = relationship("Review", backref="place",
                            cascade="delete")
    amenity = relationship("Amenity", secondary="place_amenity",
                            viewonly=False)

    if getenv('HBNB_TYPE_STORAGE', None) != 'db':
        @property
        def reviews(self):
            """ returns list of Review objects """
            from models import storage
            from models.review import Review
            review_l = []
            all_reviews = storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    review_l.append(review)
            return review_l

        @property
        def amenities(self):
            """ returns list of Amenity objects """
            from models import storage
            from models.amenity import Amenity
            amenities_l = []
            all_amenities = storage.all(Amenity)
            for amenity in all_amenities.values():
                if amenity.id == self.id:
                    amenities_l.append(amenity)
            return amenities_l
        
        @amenities.setter
        def amenities(self, value):
            """ sets amenity_ids to a list of Amenity ids """
            from models.amenity import Amenity
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
