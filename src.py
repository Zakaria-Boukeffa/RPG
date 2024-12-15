class Personnage:
    def __init__(self, endurance: int = 0, speed: int = 0):
        self.base_hp = 10  
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

    def est_mort(self):
        return self.hp == 0

    def se_soigner(self):
        if self.hp < 10:
            self.hp += 1
    
    def attaque_critique(self, defenseur):
            defenseur.hp -= 3
            
    def attaque_fumble(self, defenseur):
        self.hp -= 1
        
class Battle :
    def create_random_group():
        group = []
        for _ in range(10):
            personnage = Personnage()
            group.append(personnage)
        return group