#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class which contains __tablename__, name"""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    def cities(self):
        """Return the list of city objects from storage
        linked to the current state"""
        from models import storage
        from models.city import City
        city_list = []
        if storage.__class__.__name__ != 'DBStorage':
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
        else:
            for city in self.cities:
                city_list.append(city)
        return city_list
