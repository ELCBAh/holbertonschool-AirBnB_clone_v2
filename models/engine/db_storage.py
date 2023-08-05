#!/usr/bin/python3
"""DBStorage engine definition"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import (create_engine)
from sqlalchemy.orm import (scoped_session, sessionmaker)
from os import getenv


classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class DBStorage:
    """DBStorage engine definition class"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiation of DBStorage engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')),
                pool_pre_ping=True)
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns the dictionary of the current database session"""
        if cls is None:
            return self.__session.query(State).all()
        else:
            return self.__session.query(cls).all()

    def new(self, obj):
        """Adds new object to current database session"""
        self.__session.add(obj)

    def save(self):
        """Saves all changes of current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes current database session object"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads database session"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()

    def close(self):
        """Closes database session"""
        self.__session.close()
