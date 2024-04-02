# In Jesus name!
class Monster:
    def __init__(self, name: str, health: int, attack_power: int):
        self.name = name
        self.health = health 
        self.attack_power = attack_power

    def attack(self, target):
        target.take_damage(self.attack_power)
    
    @property
    def take_damage(self, amount):
        self.health -= amount

    def is_alive(self):
        return self.health > 0

class Player:
    def __init__(self, name: str, health: int, attack_power: int):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def take_damage(self, amount):
        self.health -= amount

    def is_alive(self):
        return self.health > 0

# Instantiate a player and a monster
p1 = Player(name='Aiza', health=200, attack_power=100)
m1 = Monster(name='Christina', health=100, attack_power=200)

# The monster attacks the player
m1.attack(p1)
print(p1.health)  # Corrected attribute access

