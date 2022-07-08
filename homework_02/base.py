from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight=100, fuel=0, fuel_consumption=5):
        self.started = False
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.fuel <= 0:
            raise LowFuelError("Fuel should be > 0")
        self.started = True

    def move(self, distance):
        required_fuel = distance * self.fuel_consumption
        if required_fuel > self.fuel:
            raise NotEnoughFuel("Not enough fuel to proceed")
        self.fuel -= required_fuel
