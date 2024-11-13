class Personnage:
    def __init__(self):
        self.hp = 10

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