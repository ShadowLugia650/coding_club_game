import sys
sys.path.insert(0, 'dependencies')
import baseM, itemStats

class Junior(baseM.basicEnemy):
    def __init__ (self):
        self.type="Ohgur"
        self.baseDamage=3
        self.baseDef=2
        self.maxHp=70
        self.health=70
        self.options = {"Kick":7, "Slash":12}
        self.loot=[itemStats.ohgurGuts(), itemStats.ohgurGuts()]
        
        
def run (player):
    print("A raging, drooling Ohgur charges at you!")
    baseM.runBasicFight(player, [Junior()],0,True)
    return player
