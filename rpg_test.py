import unittest
from src import Personnage
class TestPersonnage(unittest.TestCase):
    
    def test_perso_10_creation(self):
        personnage = Personnage()
        self.assertEqual(personnage.get_hp(), 10)
        
    def test_attaque(self):
         Perso_att = Personnage()
         Perso_defen = Personnage() 
         Perso_defen.recevoir_attaque(Perso_att)
         self.assertEqual(Perso_defen.get_hp(), 9)


if __name__ == '__main__':
    unittest.main()