#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place, place_amenity
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenity"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity")
