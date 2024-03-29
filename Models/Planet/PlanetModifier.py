"""
Implementation of PlanetModifier class
"""

from abc import ABC, abstractmethod


# todo make it more diverse once colony is implemented: affecting production, population etc.
class PlanetModifier(ABC):
    name: str

    @abstractmethod
    def apply(self, planet) -> None:
        planet.modifiers.append(self)

    @abstractmethod
    def remove(self, planet) -> None:
        if self not in planet.modifiers:
            raise KeyError(f'Cannot remove modifier {self.name} from planet {planet.name}: planet doesnt have it.')
        planet.modifiers.remove(self)


class SentientLifePlanetModifier(PlanetModifier):
    def __init__(self):
        self.name = 'Sentient life present, less space for us. But they are cute!'

    def apply(self, planet) -> None:
        super().apply(planet)
        planet.size -= 2

    def remove(self, planet) -> None:
        # You. Monster.
        super().remove(planet)
        planet.size += 2


class RichMineralsPlanetModifier(PlanetModifier):
    def __init__(self):
        self.name = 'Rich minerals, we can produce more thingies!'

    def apply(self, planet) -> None:
        super().apply(planet)
        planet.size += 1

    def remove(self, planet) -> None:
        super().remove(planet)
        planet.size -= 1


class RockPlanetModifier(PlanetModifier):
    def __init__(self):
        self.name = 'Rock planet, easy to live, hard to get resources'

    def apply(self, planet) -> None:
        super().apply(planet)
        planet.size += 1

    def remove(self, planet) -> None:
        super().remove(planet)
        planet.size -= 1


class GasPlanetModifier(PlanetModifier):
    def __init__(self):
        self.name = 'Gas planet, hard to live, easy to get resources'

    def apply(self, planet) -> None:
        super().apply(planet)
        planet.size -= 1

    def remove(self, planet) -> None:
        super().remove(planet)
        planet.size += 1


class HomePlanetModifier(PlanetModifier):
    def __init__(self):
        self.name = 'Home world, morale boost included'

    def apply(self, planet) -> None:
        super().apply(planet)
        planet.size += 2

    def remove(self, planet) -> None:
        super().remove(planet)
        planet.size -= 2
