#!/usr/bin/python3
from sqlalchemy import create_engine, ForeignKey, Column, Table, String
from sqlalchemy.orm import relationship
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
import os
from sqlalchemy.orm import sessionmaker, scoped_session
from urllib.parse import quote_plus
from models.base_model import Base


State.cities = relationship(City, cascade="all, delete",
                            back_populates="states")

City.states = relationship(State, back_populates="cities")
City.places = relationship(Place, cascade="all, delete",
                           back_populates="cities")

User.places = relationship(Place, back_populates="users",
                           cascade="all, delete")
User.reviews = relationship(Review, back_populates="users")

Place.users = relationship(User, back_populates="places")
Place.cities = relationship(City, back_populates="places")
Place.reviews = relationship(Review, back_populates="places",
                             cascade="all, delete")

Review.users = relationship(User, back_populates="reviews")
Review.places = relationship(Place, back_populates="reviews")


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id',String(60),
                             ForeignKey('places.id'), primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False))
Place.amenities = relationship("Amenity",
                               secondary=place_amenity,
                               back_populates="place_amenities",
                               viewonly=False)
Amenity.place_amenities = relationship("Place",
                                       secondary=place_amenity,
                                       back_populates="amenities",
                                       viewonly=False)

class DBStorage:
    """Database Storage to be used instead of FileStorage"""
    __engine = None
    __session = None

    def __init__(self):
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                        expire_on_commit=False))
        HBNB_MYSQL_USER = os.environ['HBNB_MYSQL_USER']
        HBNB_MYSQL_PWD = os.environ['HBNB_MYSQL_PWD']
        HBNB_MYSQL_HOST = os.environ['HBNB_MYSQL_HOST']
        HBNB_MYSQL_DB = os.environ['HBNB_MYSQL_DB']
        self.__engine = create_engine(f"mysql+mysqldb://"
                                      f"{quote_plus(HBNB_MYSQL_USER)}"
                                      f":{quote_plus(HBNB_MYSQL_PWD)}"
                                      f"@{quote_plus(HBNB_MYSQL_HOST)}"
                                      f":3306/{quote_plus(HBNB_MYSQL_DB)}",
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        objs = None
        if cls is None:
            objs = self.__session.query()
        else:
            objs = self.__session.query(cls)
        dct = {}

        for obj in objs:
            key = obj.to_dict()['__class__'] + '.' + obj.id
            dct[key] = obj
        return dct

    def new(self, obj):
        """ Adds the obj to the current database session(self.__session)"""
        self.__session.add(obj)

    def save(self):
        """ Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj):
        """deletes obj from the current db session if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                        expire_on_commit=False))
        self.__session.commit()

    def close(self):
        """Function call from self.__session"""
        self.__session.remove()
