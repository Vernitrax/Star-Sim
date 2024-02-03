"""
Implementation of PlanetModifier class
"""

from abc import ABC


class PlanetModifier(ABC):
    pass


class SentientLifePlanetModifier(PlanetModifier):
    pass


class RichMineralsPlanetModifier(PlanetModifier):
    pass


class RockPlanetModifier(PlanetModifier):
    pass


class GasPlanetModifier(PlanetModifier):
    pass
