import sys, random

sys.path.insert(0, 'dependencies')
import baseM

class DemonicWarrior(baseM.basicEnemy):
    def __init__(self):
        self.type = "Demonic Warrior"
        self.baseDamage = 7
        self.baseDef = 20
        self.health = 110
        self.maxHp = 110
        self.loot = [("Gold", random.randint(100,150))]
        self.options = {"Slash":0, "Strike":5, "Double Strike":-10}

    def move(self):
        self.baseDamage += 3
        atk = random.choice(list(self.options.keys()))
        if atk == "Double Strike":
            return atk, ((self.baseDamage+self.options[atk])*2)
        return atk, (self.baseDamage + self.options[atk])

def run(player):
    print("You encountered the Demonic warrior!")
    enemies = [DemonicWarrior()]
    input("The Demonic Warrior engages you in combat!")
    baseM.runBasicFight(player, enemies)
    return player
