#this script is for curses, which are player debuffs that last until dispelled by special effects.

import random, itemStats, baseM

class basicCurse(itemStats.basicItem): #although the curse is not necessarily an item, using extension makes it have all these attributes without requiring copy paste
    def __init__(self):
        self.name = None
        self.desc = ""
        self.effectText = ""
        self.target = None

    def onCombatTurn(self, player):
        pass

    def printEffect(self):
        baseM.showText(self.effectText,screen)
    
    def curseItem(self, item):
        self.target = item
        
    def remove(self, player):
        player.curses.remove(self)

#Player curses
class exhaustion(basicCurse):
    def __init__(self):
        self.severity = 1
        self.name = "Exhaustion level: " + str(self.severity)
        self.desc = "Mental and physical fatigue from lack of sleep."

    def onCombatTurn(self, player):
        choice = random.randint(1, 2)
        fatigue = random.randint(1, self.severity)
        Type = ""
        if choice == 1:
            self.effectText = "Exhaustion saps your strength!" #instead of using self.effectText and self.printEffect(), you could just put these as prints...
            Type = "Damage"
        else:
            self.effectText = "Exhaustion drains your dexterity!"
            Type = "Block"
        self.printEffect()
        return fatigue, Type

    def onFloorClimb(self, player):
        self.severity += 1

class toxins(basicCurse):
    def __init__(self):
        self.severity = 8
        self.name = "Toxins: {}".format(self.severity)
        self.desc = "Toxic compounds deal damage over time if not treated and deal more damage if you are exhausted.."
        
    def toxinDamage(self, player):
        dmg = self.severity
        baseM.showText("The toxins damage you for {} hp!".format(dmg),screen)
        for i in player.curses:
            if type(i) == exhaustion:
                dmg += i.severity
                baseM.showText("Your exhaustion increases the effectiveness of the toxins!",screen)
        return dmg
        
    def onCombatTurn(self, player):
        dmg = round(self.toxinDamage(player, screen)*0.75)
        player.health -= dmg
        
    def onFloorClimb(self, player):
        dmg = self.toxinDamage(player, screen)
        player.health -= dmg
        self.severity -= 1
        if self.severity == 0:
            player.curses.remove(self)
        
class hubris(basicCurse):
    def __init__(self):
        self.name = "Hubris"
        self.desc = "Allows impossible rooms to naturally occur"
    
    def onFloorClimb(self, player):
        if not player.impossible:
            player.impossible = True
    
    def remove(self, player):
        player.impossible = False
        player.curses.remove(self)

class stupidity(basicCurse):
    def __init__(self):
        self.name = "Stupidity"
        self.desc = "Me stupid. Stupid Sword Strong"
        self.justAdded = True
        self.affectedSwords = []
        
    def onFloorClimb(self, player):
        if self.justAdded:
            self.justAdded = False
            for i in player.items:
                if i.name == "Sword of Stupidity":
                    i.damage *= 3
                    self.affectedSwords.append(i)
        else:
            for i in player.items:
                if i.name == "Sword of Stupidity" and i not in self.affectedSwords:
                    i.damage *= 3
                    self.affectedSwords.append(i)
                    
    def remove(self, player):
        for i in self.affectedSwords:
            i.damage /= 3
        player.curses.remove(self)

class nameMe(basicCurse):
    def __init__(self):
        self.name = "" #Merciric absorption thing//alcoholism
        self.desc = "The enemy of the wealthy and the poor alike."
        
    def onFloorClimb(self, player):
        player.gold -= round(player.gold*0.1)
        
class madness(basicCurse):
    def __init__(self):
        self.name = "Madness"
        self.desc = "Yes yes yes yes yes yes yes."
        
    def onFloorClimb(self, player):
        c = random.randint(1,2) # add 3 later
        if c == 1:
            dmg = random.randint(3,6)
            player.health -= dmg
            baseM.showText("You took {} damage".format(dmg),screen)
        elif c == 2:
            itm = random.choice(player.items)
            baseM.showText("You lost your {}".format(itm.name),screen)
        elif c == 3:
            pass #randomly generate an item to add to inventory
        
#Item curses
class ephemeral(basicCurse):
    def __init__(self):
        self.floorsLeft = 10
        self.name = "Ephemeral: {}".format(self.floorsLeft)
        self.desc = "The ephemeral and fragile nature of human life is infused into this item."
        self.target = None
        
    def onFloorClimb(self, player):
        self.floorsLeft -= 1
        if self.floorsLeft == 0:
            player.items.remove(self.target)
   
class steelblight(basicCurse):
    def __init__(self):
        self.name = "Steelblight"
        self.desc = "The ultimate scourge of shopkeepers and collectors, this curse enbrittles even the hardest steel, and spreads from item to item."
        self.target = []
        
    def curseItem(self, player): #this shouldbe curseItem(self, item)... we can handle the random choice when the curse is applied.
        if player.items != null:
            random.choice(player.items)








