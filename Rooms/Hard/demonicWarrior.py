import sys, random

sys.path.insert(0, 'dependencies')
import baseM
from itemStats import demonicSword

class DemonicWarrior(baseM.basicEnemy):
    def __init__(self):
        self.type = "Demonic Warrior"
        self.baseDamage = 7
        self.baseDef = 20
        self.health = 200
        self.maxHp = 200
        self.loot = [("Gold", random.randint(100,150)), demonicSword()]
        self.options = {"Slash":0, "Strike":5, "Double Strike":-10, "Amplify":0}
        self.optionsP2 = {"Strike":5, "Double Strike":-6, "Combo Slash":0}
        self.phase = 1

    def move(self):
        if self.health <= 55 and self.phase == 1:
            print("\"You will never defeat me!\"")
            self.baseDamage += 10
            self.phase = 2
            self.health += 10
        if self.baseDamage >= 24 and self.baseDamage <= 26:
            print("\"HAHAHAHAHAHAHAHA\"")
        self.baseDamage += 3
        if self.phase == 1:
            atk = random.choice(list(self.options.keys()))
            if atk == "Amplify":
                self.baseDamage *= 2
                return atk, 0
        elif self.phase == 2:
            atk = random.choice(list(self.optionsP2.keys()))
            if atk == "Combo Slash":
                return "{} ({},{},{})".format(atk,(self.baseDamage),(self.baseDamage-5),(self.baseDamage+8)), ((self.baseDamage)+(self.baseDamage-5)+(self.baseDamage+8))
        if atk == "Double Strike":
            return "{} ({}x2)".format(atk,(self.baseDamage+self.options[atk])), ((self.baseDamage+self.options[atk])*2)
        return atk, (self.baseDamage + self.options[atk])

def run(player):
    print("You encountered the Demonic warrior!")
    enemies = [DemonicWarrior()]
    input("The Demonic Warrior engages you in combat!")
    baseM.runBasicFight(player, enemies)
    return player
