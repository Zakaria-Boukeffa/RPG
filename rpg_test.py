import unittest
from src import Personnage, Battle 
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
    
    def test_personnage_peut_se_soigner(self):
        personnage = Personnage()
        personnage.recevoir_attaque(None)  
        personnage.se_soigner()  
        self.assertEqual(personnage.get_hp(), 10)
    
    def test_attaque_critique(self):
        attaquant = Personnage()
        deffenseur = Personnage()
        attaquant.attaque_critique(deffenseur)
        self.assertEqual(deffenseur.get_hp(), 7) 

    def test_attaque_fumble(self):
        attaquant = Personnage()
        deffenseur = Personnage()    
        attaquant.attaque_fumble(deffenseur)
        self.assertEqual(attaquant.get_hp(), 9)

    def test_Endurance_Level(self):
        personnage = Personnage(endurance=1)
        self.assertEqual(personnage.hp, 12)
        
    def test_Speed_Level(self):
        personnage = Personnage(speed=1)
        self.assertEqual(personnage.speed, 1)

    def test_create_random_group(self):
        group = Battle.create_random_group()
        self.assertEqual(len(group), 10)

    def test_sort_by_speed(self):
        group = Battle.create_random_group()
        sorted_group = Battle.sort_by_speed(group)
        for i in range(len(sorted_group) - 1):
            self.assertGreaterEqual(sorted_group[i].speed, sorted_group[i+1].speed)


    def test_full_battle(self):
        group = Battle.create_random_group()  
        sorted_group = Battle.sort_by_speed(group)  
        alive_count = Battle.full_battle(sorted_group) 
        self.assertEqual(alive_count, 1)

if __name__ == '__main__':
    unittest.main()