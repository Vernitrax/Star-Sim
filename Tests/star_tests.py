import unittest

from Models.Star.Star import Star


class TestStar(unittest.TestCase):
    def test_singleton_identity(self):
        s1 = Star.instance()
        s2 = Star.instance()
        self.assertTrue(s1 is s2)

    def test_singleton_create_new(self):
        with self.assertRaises(TypeError):
            Star()

    def test_starting_cycle_value(self):
        Star.instance()
        self.assertEqual(100, Star.instance()._cycles_to_supernova)

    def test_decrementing_cycle(self):
        cycles = Star.instance()._cycles_to_supernova
        self.assertEqual(cycles, Star.instance()._cycles_to_supernova)
        Star.instance().do_cycle()
        self.assertEqual(cycles - 1, Star.instance()._cycles_to_supernova)
        Star._cycles_to_supernova = cycles

    def test_supernova(self):
        cycles = Star.instance()._cycles_to_supernova
        for i in range(cycles - 1):
            self.assertEqual(cycles - i, Star.instance()._cycles_to_supernova)
            Star.instance().do_cycle()
        self.assertEqual(1, Star.instance()._cycles_to_supernova)
        with self.assertRaises(SystemExit):
            Star.instance().do_cycle()
        self.assertEqual(0, Star.instance()._cycles_to_supernova)
        Star._cycles_to_supernova = cycles
