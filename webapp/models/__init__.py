from flask_mongoengine import MongoEngine
from flask import Flask

db = MongoEngine()


def init_db(app: Flask):
    db.init_app(app)

from .user_model import User
from .camera_model import Camera
from .parking_model import ParkingArea
from .event_model import AnomalyEvent
