#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class which contains __tablename__, name"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Return the list of city objects from storage
            linked to the current state"""
            city_list = []
            sum_cities = models.storage.all(City)
            for city in sum_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
    
    def __init__(self, *args, **kwargs):
        """initializes State"""
        super().__init__(*args, **kwargs)
