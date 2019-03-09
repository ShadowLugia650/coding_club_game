import sys
sys.path.insert(0, 'dependencies')
import baseM

class Junior(baseM.basicEnemy):
    def __init__ (self):
        self.type="Ohgur"
        self.baseDamage=17
        self.baseDef=2
        self.maxHp=45
        self.health=45
        self.options = {"Kick":7, "Slash":10}
        self.loot=[("Nails",random.randint(10,20))]
        
        
def run (player):
    print("A raging, drooling Ohgur charges at you!")
    baseM.runBasicFight(player, [Junior()],0,True)
    return player
