#!/usr/bin/python3
""" City Module for HBNB project """
import string
from tkinter import CASCADE
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__="cities"
    name = Column(string(128), nullable=False)
    state_id = Column(string(60), ForeignKey('states.id'), nullable=False)
    places = relationship("place", backref="cities", CASCADE="all, delete")