#!/usr/bin/python3
""" State Module for HBNB project """
import string
from tkinter import CASCADE
from models import city
from models.base_model import BaseModel,Base
from sqlalchemy import column, String, Integer, DateTime,ForeignKey
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    name = column(string(128), nullable=False)
    cities = relationship("city", backref="state",
                            CASCADE="all, delete-orphan"
    )

    @property
    def cities(self):
        # getter attribute cities that retutns the list of city
        from models import storage
        my_list =[]
        extracted_cities = storage.all(City).values()
        for city in extracted_cities:
            if self.id == City.state_id:
                my_list.append(City)
        return my_list
