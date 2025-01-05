

class Movement:
    def __init__(self,name, damage, probability_success_attack):
        self.name = name
        self.damage = damage
        self.probability_success_attack = probability_success_attack

class Character:
    def __init__(self,level,health, strength, agility, movements,special_attack,defenses):
        self.level = level
        self.health = health
        self.damage = strength
        self.agility = agility
        self.movements = movements
        self.special_attack = special_attack
        self.defenses = defenses

    def make_move(self,):
        pass


       

