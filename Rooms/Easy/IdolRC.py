import baseM, random, itemStats

def run(player):
    print("A golden idol stands in the middle of the hallway")
    print("Hack pieces off or touch the idol?")
    choice = input("[hack pieces, touch idol]")
    thisIdol = Idol()
    if choice.lower() in ["hack pieces","hack", "h"]:
        baseM.runBasicFight(player, [thisIdol], 0, True, 5)
        print("You broke "+str(round((1000-thisIdol.health())/2))+" worth of gold fragments off the idol!")
        player.gold+=round((1000-thisIdol.health())/2)
        return player
    elif choice.lower() in ["touch idol","touch", "t"]:
        print("The idol shrinks in size until it can fit in your backpack")
        player.items.append(itemStats.idol())
        return player

class Idol(baseM.basicEnemy):
    def __init__ (self):
        self.type="Idol"
        self.maxHp=1000
        self.health=1000
        self.baseDamage=0
        self.baseDef = 0
        self.block = 0
        self.options = {"Glow":0}
        self.loot=[itemStats.idolShield()]
        
