"""
Implementation of Resource Field Factory class -> applying factory pattern
"""

import random

from abc import ABC, abstractmethod

from . import ResourceField


class ResourceFieldFactory(ABC):
    gas_chance: float

    @abstractmethod
    def factory_method(self) -> ResourceField.ResourceField:
        pass


class RichResourceFieldFactory(ResourceFieldFactory):
    def __init__(self):
        self.gas_chance = 0.7

    def factory_method(self) -> ResourceField.ResourceField:
        is_gas = random.random() < self.gas_chance
        new_size = random.randint(1, 3)
        return ResourceField.GasCloud(new_size) if is_gas else ResourceField.AsteroidField(new_size)


class BalancedResourceFieldFactory(ResourceFieldFactory):
    def __init__(self):
        self.gas_chance = 0.5

    def factory_method(self) -> ResourceField.ResourceField:
        is_gas = random.random() < self.gas_chance
        new_size = random.randint(1, 3)
        return ResourceField.GasCloud(new_size) if is_gas else ResourceField.AsteroidField(new_size)


class SparseResourceFieldFactory(ResourceFieldFactory):
    def __init__(self):
        self.gas_chance = 0.3

    def factory_method(self) -> ResourceField.ResourceField:
        is_gas = random.random() < self.gas_chance
        new_size = random.randint(1, 3)
        return ResourceField.GasCloud(new_size) if is_gas else ResourceField.AsteroidField(new_size)
