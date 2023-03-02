from .car import Car
from .bike import Bike
from .truck import Truck


class Factory:

    def getVehicleObject(self, type):
        if type == "CAR":
            return Car()
        elif type == "BIKE":
            return Bike()
        elif type == "TRUCK":
            return Truck()
        else:
            return None
