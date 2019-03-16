import sys, random

sys.path.insert(0, 'dependencies')
import baseM

#class 

class Necromancer(baseM.basicEnemy):
    def __init__(self):
        self.type = "Necromancer"
        self.baseDef = 0
        self.block = 0
        self.health = 200
        self.maxHp = 200
        self.overhealCapacity = 300
        self.baseDamage = 100
        self.loot = []
        self.options = {"Summon: ":0}
        self.optionsP2 = dict(self.options, **{"Heal":0})
        self.picklist = self.options
        
    def move(self, player):
        if (self.health <= self.maxHp/2):
            self.picklist = self.optionsP2
        else:
            self.picklist = self.options
        atk = random.choice(self.picklist.keys())
        if "Summon: " in atk:
            summonText = atk.split("Summon: ")[1]
            summon = eval(baseM.strToClsNm(summonText))()
            return atk, summon
        elif atk == "":
            return atk, 0
        return atk, self.baseDamage + self.options[atk]
        
def run(player, screen):
    return player





