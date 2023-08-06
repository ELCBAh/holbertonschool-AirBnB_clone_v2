#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def _cities(self):
            """getter for list of City instances with state_id == current State.id"""
            city_l = []
            from models import storage
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_l.append(city)
            return city_l
