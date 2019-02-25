import sys, random

sys.path.insert(0, 'dependencies')
import baseM

class Necromancer(baseM.basicEnemy):
    def __init__(self):
        self.type = "Necromancer"
        self.health = 200
        self.maxHealth = 300
        
def run(player):
    return player
