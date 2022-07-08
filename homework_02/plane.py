"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo: int

    def __init__(self, weight=1000, fuel=0, fuel_consumption=10, max_cargo=10):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, cargo):
        total_cargo = self.cargo + cargo
        if total_cargo > self.max_cargo:
            raise CargoOverload("Total cargo must be <= max_cargo")
        self.cargo = total_cargo

    def remove_all_cargo(self):
        cargo = self.cargo
        self.cargo = 0
        return cargo
