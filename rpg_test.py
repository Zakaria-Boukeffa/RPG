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
         
    def test_personnage_meurt_a_0_hp(self):
        personnage = Personnage()
        for _ in range(10):  
            personnage.recevoir_attaque(None)
        self.assertTrue(personnage.est_mort())  

if __name__ == '__main__':
    unittest.main()