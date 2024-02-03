"""
Planet class implementation
"""

from abc import ABC, abstractmethod

from PlanetModifier import PlanetModifier, RockPlanetModifier, GasPlanetModifier, HomePlanetModifier


class Planet(ABC):
    name: str
    size: int
    is_colonized: bool = False
    modifiers: list[PlanetModifier, ...]
    # colony: Colony   todo replace with actual Colony implementation

    @abstractmethod
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    @abstractmethod
    def colonize(self) -> None:
        self.is_colonized = True
        # self.Colony = colony


class RockPlanet(Planet):
    def __init__(self, name: str, size: int):
        super().__init__(name, size)
        rock_mod = RockPlanetModifier()
        rock_mod.apply(self)
        self.modifiers.append(rock_mod)

    def colonize(self) -> None:
        super().colonize()
        # todo apply some bonus/penalty from rock planet origin


class GasPlanet(Planet):
    def __init__(self, name: str, size: int):
        super().__init__(name, size)
        gas_mod = GasPlanetModifier()
        gas_mod.apply(self)
        self.modifiers.append(gas_mod)

    def colonize(self) -> None:
        super().colonize()
        # todo apply some bonus/penalty from gas planet origin


class Home(Planet):
    def __init__(self, name: str, size: int = 5):
        super().__init__(name, size)
        home_mod = HomePlanetModifier()
        home_mod.apply(self)
        self.modifiers.append(home_mod)
        self.colonize()

    def colonize(self) -> None:
        super().colonize()
        # new_colony = HomeColony()
        # super().colonize(new_colony)
        # todo apply some bonus/penalty from home planet origin
