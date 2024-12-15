import random

class Personnage:
    def __init__(self, name: str = '', endurance: int = 0, speed: int = 0):
        self.base_hp = 10  
        self.name = name 
        self.endurance = endurance  
        self.speed = speed
        self.hp = self.calculate_hp()

    def calculate_hp(self):
        return self.base_hp + (self.endurance * 2)
  
    def get_hp(self):
        return self.hp

    def recevoir_attaque(self, attaquant):
        if self.hp > 0:
            self.hp -= 1
            self.hp = max(0, self.hp) 

   

    def est_mort(self):
        return self.hp <= 0

    def se_soigner(self):
        if self.hp < 10:
            self.hp += 1
    
    def attaque_critique(self, defenseur):
        defenseur.hp -= 3
        defenseur.hp = max(0, defenseur.hp)

            
    def attaque_fumble(self, defenseur):
        self.hp -= 1
        self.hp = max(0, self.hp)

        
class Battle :
    
    def create_random_group():
        group = []
        for i in range(10):
            endurance = random.randint(0, 5)
            speed = random.randint(1, 3)
            name = f"Personnage_{i}" 
            personnage = Personnage(name=name, endurance=endurance, speed=speed)  
            group.append(personnage)
        return group
    
    def sort_by_speed(group):
        return sorted(group, key=lambda x: x.speed, reverse=True)
