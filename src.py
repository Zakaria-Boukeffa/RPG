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

    def full_battle(group):
        alive_count = len(group) 
        while alive_count > 1: 
            for attacker in group: 
                if attacker.est_mort():
                    continue
                
                possible_defenders = [p for p in group if p != attacker]
                if not possible_defenders:
                    continue
                
                print(f"Alive characters: {alive_count} \n")
                
                defender = random.choice(possible_defenders)
                attack_type = random.randint(0, 2) 
                
                if attack_type == 0:
                    defender.recevoir_attaque(attacker)
                elif attack_type == 1:
                    attacker.attaque_critique(defender)
                elif attack_type == 2:
                    attacker.attaque_fumble(defender)

                if defender.est_mort():
                    alive_count -= 1
                
                print(f"{attacker.name} attacked {defender.name}.")
                print(f"{defender.name} HP: {defender.get_hp()}")
                
                if alive_count == 1:
                    print(f"{attacker.name} is the winner")
                    break 
        return alive_count