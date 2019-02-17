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
        self.options = {"Consume":0, ""}
        
    def move(self):
        atk = random.choice(list(self.options.keys()))
        return atk, self.options[atk]+self.baseDamage

def run(player):
    t = timeEater()
    enemies = [t]
    if len(player.items) > 50:
        t.baseDamage = 15
    t.baseDamage *= player.timeClimbing
    print("You walk into a large spacious room. There are clocks all over the walls, each with a different name on it.")
    print("As you continue walking you see your name. Suddenly, the clock starts to grow, and the hands reach out toward you.")
    
    return player
