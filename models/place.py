#!/usr/bin/python3
'''Class Place that inherits from BaseMode
'''
#from models.base_model import BaseModel

class Place:

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

if __name__ == "main":
    print(Place.city_id)
    print('------------------------')
    print(Place.user_id)
    print('------------------------')
    print(Place.name)
    print('------------------------')
    print(Place.description)
    print('------------------------')
    print(Place.number_rooms)
    print('------------------------')
    print(Place.number_bathrooms)
    print('------------------------')
    print(Place.number_rooms)
    print('------------------------')
    print(Place.max_guest)
    print('------------------------')
    print(Place.price_by_night)
    print('------------------------')
    print(Place.latitude)
    print('------------------------')
    print(Place.longitude)
    print('------------------------')
    print(Place.amenity_ids)
    print('------------------------')