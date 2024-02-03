"""
Implementation of Planet Factory class -> applying factory pattern
"""

import random

from abc import ABC, abstractmethod

from Planet import RockPlanet, GasPlanet
from PlanetModifier import SentientLife, RichMinerals


planet_names = (
    'Havaihiri', 'Tolmonov', 'Pistrone', 'Inrarth', 'Taliv', 'Niturn', 'Thoirus', 'Bathunus', 'Bion G48W', 'Goria 7',
    'Ozionope', 'Cidranerth', 'Sidrurn', 'Zutrone', 'Cialara', 'Aerilia', 'Vulanerth', 'Trovinope', 'Theshan MK',
    'Ciri 2H64',
)


class PlanetFactory(ABC):
    min_size: int
    max_size: int

    @abstractmethod
    def factory_method(self):
        pass


class BalancedPlanetFactory(PlanetFactory):
    def __init__(self):
        self.min_size = 4
        self.max_size = 6

    def factory_method(self):
        new_size = random.randint(self.min_size, self.max_size)
        new_name = random.choice(planet_names)
        new_type = random.choice((RockPlanet, GasPlanet))
        product = new_type(new_name, new_size)
        new_modifier = random.choice((None, SentientLife, RichMinerals))
        if new_modifier is not None:
            product.modifiers.append(new_modifier)
            new_modifier.apply(product)
        return product


class SmallPlanetFactory(PlanetFactory):
    def __init__(self):
        self.min_size = 2
        self.max_size = 4

    def factory_method(self):
        new_size = random.randint(self.min_size, self.max_size)
        new_name = random.choice(planet_names)
        new_type = random.choice((RockPlanet, RockPlanet, GasPlanet))
        product = new_type(new_name, new_size)
        new_modifier = random.choice((None, SentientLife, RichMinerals))
        if new_modifier is not None:
            product.modifiers.append(new_modifier)
            new_modifier.apply(product)
        return product


class BigPlanetFactory(PlanetFactory):
    def __init__(self):
        self.min_size = 6
        self.max_size = 8

    def factory_method(self):
        new_size = random.randint(self.min_size, self.max_size)
        new_name = random.choice(planet_names)
        new_type = random.choice((RockPlanet, GasPlanet, GasPlanet))
        product = new_type(new_name, new_size)
        new_modifier = random.choice((None, SentientLife, RichMinerals))
        if new_modifier is not None:
            product.modifiers.append(new_modifier)
            new_modifier.apply(product)
        return product
