"""
Implementation of Resource Field class
"""

from abc import ABC, abstractmethod


class ResourceField(ABC):
    size: int
    is_mined: bool = False

    @abstractmethod
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def start_mining(self):
        self.is_mined = True

    @abstractmethod
    def stop_mining(self):
        self.is_mined = False


class AsteroidField(ResourceField):
    def __init__(self, size):
        super().__init__(size)

    def start_mining(self):
        super().start_mining()

    def stop_mining(self):
        super().stop_mining()


class GasCloud(ResourceField):
    def __init__(self, size):
        super().__init__(size)

    def start_mining(self):
        super().start_mining()

    def stop_mining(self):
        super().stop_mining()
