import sys, random, time
sys.path.insert(0, 'dependencies')
import baseM

class timeEater(baseM.basicEnemy):
    def __init__(self):
        self.type = "Time Eater"
        self.baseDamage = 10
        self.health = 450
        self.maxHp = 450
        self.loot = [("Gold", random.randint(100,150))]#, HungryClock()]
        self.options = {"Consume":0, "Strike":0, "Future Doom":30, "Stall":0}
        self.optionsP2 = {"Minute Spear":"self.baseDamage+5", "Hour Skewer":"self.baseDamage*2", "Future Doom":"self.baseDamage*5", "Hasten":"0"}
        self.phase = 1
        self.turnCounter = 0
        self.timedTurn = (0, 0)
        
    def move(self):
        self.turnCounter += 1
        print("Take your time...")
        if self.phase == 1:
            if self.timedTurn[0] == (self.turnCounter - 3):
                return "Future Doom Damage", self.timedTurn[1]
            atk = random.choice(list(self.options.keys()))
            if atk == "Consume":
                self.health += self.baseDamage
                if self.health > self.maxHp:
                    self.health = self.maxHp
                dmg = 0
            elif atk == "Future Doom":
                self.timedTurn = (self.turnCounter, self.options[atk]+self.baseDamage)
                dmg = 0
            elif atk == "Stall":
                for i in range(5):
                    time.sleep(2)
                    self.baseDamage += 2
                    print('.',end='')
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
                print("")
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
