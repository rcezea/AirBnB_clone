#!/usr/bin/python3
'''Class Place that inherits from BaseMode
'''
from models.base_model import BaseModel


class Place(BaseModel):
    city_id = str()
    user_id = str()
    name = str()
    description = str()
    number_rooms = int()
    number_bathrooms = int()
    number_rooms = int()
    max_guest = int()
    price_by_night = int()
    latitude = float()
    longitude = float()
    amenity_ids = [str()]
