#this script is for curses, which are player debuffs that last until dispelled by special effects.

import random, itemStats, baseM

class basicCurse(baseM.basicItem): #although the curse is not necessarily an item, using extension makes it have all these attributes without requiring copy paste
    def __init__(self):
        self.name = None
        self.desc = ""
        self.effectText = ""
        self.target = None

    def onCombatTurn(self, player):
        pass

    def printEffect(self):
        return self.effectText
    
    def curseItem(self, item):
        self.target = item

class exhaustion(basicCurse):
    def __init__(self):
        self.severity = 1
        self.name = "Exhaustion level: " + str(self.severity)
        self.desc = "Mental and physical fatigue from lack of sleep."

    def onCombatTurn(self, player):
        choice = random.randint(1, 2)
        fatigue = random.randint(1, self.severity)
        if choice == 1:
            if player.damage > fatigue:
                player.damage -= fatigue
            else:
                player.damage = 1
            self.effectText = "Exhaustion saps your strength!"
        else:
            if player.block > fatigue:
                player.block -= fatigue
            else:
                player.block = 1
            self.effectText = "Exhaustion lowers your dexterity!"
        printEffect(self)

    def onFloorClimb(self, player):
        self.severity += 1

class ephemeral(basicCurse):
    def __init__(self):
        self.floorsLeft = 10
        self.name = "Ephemeral: {}".format(self.floorsLeft)
        self.desc = "The ephemeral and fragile nature of human life is infused with this item."
        self.target = None
        
    def onFloorClimb(self, player):
        self.floorsLeft -= 1
        if self.floorsLeft == 0:
            player.items.remove(self.target)
