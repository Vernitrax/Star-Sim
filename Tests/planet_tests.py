import unittest


class TestPlanet(unittest.TestCase):
    def test_factory_method(self):
        import Models.Planet.PlanetFactory as PlanetFactory
        factory_list = (
            PlanetFactory.BalancedPlanetFactory(),
            PlanetFactory.SmallPlanetFactory(),
            PlanetFactory.BigPlanetFactory()
        )
        for factory in factory_list:
            planet = factory.factory_method()
            try:
                planet.colonize()  # duck-typing test
            except AttributeError:
                self.fail('Planet needs to implement colonize')

    def test_apply_modifier(self):
        # todo replace when modifiers are better with more fun tests
        import Models.Planet.PlanetFactory as PlanetFactory
        import Models.Planet.PlanetModifier as PlanetModifier
        factory_list = (
            PlanetFactory.BalancedPlanetFactory(),
            PlanetFactory.SmallPlanetFactory(),
            PlanetFactory.BigPlanetFactory()
        )
        modifiers_list = (
            PlanetModifier.GasPlanetModifier(),
            PlanetModifier.RockPlanetModifier(),
            PlanetModifier.HomePlanetModifier(),
            PlanetModifier.SentientLifePlanetModifier(),
            PlanetModifier.RichMineralsPlanetModifier()
        )
        for factory in factory_list:
            planet = factory.factory_method()
            for modifier in modifiers_list:
                pre_size = planet.size
                pre_size_list = len(planet.modifiers)
                modifier.apply(planet)
                post_size = planet.size
                post_size_list = len(planet.modifiers)
                self.assertNotEqual(pre_size, post_size)
                self.assertEqual(post_size_list - pre_size_list, 1)

    def test_remove_modifier(self):
        # todo replace when modifiers are better with more fun tests
        import Models.Planet.PlanetFactory as PlanetFactory
        import Models.Planet.PlanetModifier as PlanetModifier
        factory_list = (
            PlanetFactory.BalancedPlanetFactory(),
            PlanetFactory.SmallPlanetFactory(),
            PlanetFactory.BigPlanetFactory()
        )
        modifiers_list = (
            PlanetModifier.GasPlanetModifier(),
            PlanetModifier.RockPlanetModifier(),
            PlanetModifier.HomePlanetModifier(),
            PlanetModifier.SentientLifePlanetModifier(),
            PlanetModifier.RichMineralsPlanetModifier()
        )
        for factory in factory_list:
            planet = factory.factory_method()
            for modifier in modifiers_list:
                pre_size = planet.size
                pre_size_list = len(planet.modifiers)
                modifier.apply(planet)
                modifier.remove(planet)
                post_size = planet.size
                post_size_list = len(planet.modifiers)
                self.assertEqual(pre_size, post_size)
                self.assertEqual(pre_size_list, post_size_list)

    def test_colonize(self):
        import Models.Planet.PlanetFactory as PlanetFactory
        factory_list = (
            PlanetFactory.BalancedPlanetFactory(),
            PlanetFactory.SmallPlanetFactory(),
            PlanetFactory.BigPlanetFactory()
        )
        for factory in factory_list:
            planet = factory.factory_method()
            self.assertTrue(not planet.is_colonized)
            planet.colonize()
            self.assertTrue(planet.is_colonized)
