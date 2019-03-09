import sys
sys.path.insert(0, 'dependencies')
import baseM, itemStats

class Junior(baseM.basicEnemy):
    def __init__ (self):
        self.type="Ohgur"
        self.baseDamage=2
        self.baseDef=2
        self.maxHp=2
        self.health=2
        self.options = {"Kick":5, "Slash":8}
        self.loot=[itemStats.ohgurGuts(), itemStats.ohgurGuts()]
        
        
def run (player):
    print("A raging, drooling Ohgur charges at you!")
    baseM.runBasicFight(player, [Junior()],0,True)
    return player
