import unittest
from src import Personnage
class TestPersonnage(unittest.TestCase):
    def test_perso_10_creation(self):
        personnage = Personnage()
        self.assertEqual(personnage.get_hp(), 10)


if __name__ == '__main__':
    unittest.main()