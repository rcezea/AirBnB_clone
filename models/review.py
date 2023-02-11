#!/usr/bin/python3
'''Class Review that inherits from BaseMode
'''
from models.base_model import BaseModel


class Review(BaseModel):
    place_id = str()
    user_id = str()
    text = str()
