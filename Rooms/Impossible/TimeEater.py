import sys, random
sys.path.insert(0, 'dependencies')
import baseM

class timeEater(baseM.basicEnemy):
    def __init__(self):
        self.type = "Time Eater"
        self.baseDamage = 10
        self.health = 450
        self.maxHp = 450
        self.loot = [("Gold", random.randint(100,150))]#, HungryClock()]
        self.options = {"Consume":0, "":1}
        self.optionsP2 = {"Minute Spear":"self.baseDamage+5", "Hour Skewer":"self.baseDamage*2"}
        self.phase = 1
        
    def move(self):
        if self.phase == 1:
            atk = random.choice(list(self.options.keys()))
            if atk == "Consume":
                self.health += self.baseDamage
                if self.health > self.maxHp:
                    self.health = self.maxHp
                dmg = 0
            else:
                dmg = self.options[atk]+self.baseDamage
        elif self.phase == 2:
            atk = random.choice(list(self.optionsP2.keys()))
            hit = True
            if atk == "Hour Skewer":
                hit = random.randint(1,100)<75
            if hit:
                dmg = eval(self.optionsP2[atk])
            else:
                dmg = 0
        return atk, dmg

def run(player):
    t = timeEater()
    enemies = [t]
    if len(player.items) > 50:
        t.baseDamage = 15
    t.baseDamage *= player.timeClimbing
    print("You walk into a large spacious room. There are clocks all over the walls, each with a different name on it.")
    print("As you continue walking you see your name. Suddenly, the clock starts to grow, and the hands reach out toward you.")
    
    return player
