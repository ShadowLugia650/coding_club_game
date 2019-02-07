#Basic Item Classes, extend these.
class basicItem():
    def __init__(self):
        self.name = None
        self.desc = ""

    def __str__(self):
        return self.name

    def readDesc(self):
        print(self.desc)

class basicSword(basicItem):
    def __init__(self):
        self.name = "Sword"
        self.desc = "A weapon, I think."
        self.damage = 10

    def boostDamage(self, initial):
        return initial+self.damage

class basicDefensiveItem(basicItem):
    def __init__(self):
        self.name = "Shield"
        self.desc = "Use it"
        self.block = 10
       
    def boostDefense(self, defense):
        return defense+self.block

class basicMagicItem(basicItem):
    # Magic Items should have a function to replace donothing in self.magic. This function will run whenever a player chooses the magic option in a fight
    def donothing():
        print("")
    def __init__(self):
        self.name = "Magic Item"
        self.desc = "Abracadabra! Use this item in combat for special abilities"
        self.magic = donothing()

#Testing stuff: remove later
class testerSword(basicSword):
    def __init__(self):
        self.name = "Tester Sword"
        self.desc = "Testing testing.."
        self.damage = 1000
        
#Regular Items
class firstLetter(basicItem):
    def __init__(self):
        self.name = "Letter From the Deceased"
        self.desc = """The letter is tattered and some words are missing.
The faded words read:
Deare
If th   lett r  as rea hed you  I  m pr bably de d.
[]
 ov
"""

class corruptBlood(basicItem):
    def __init__(self):
        self.name = "Corrupt Blood"
        self.desc = "A strange bluish-purple liquid..."

    def onFloorClimb(self, player):
        player.health += 10

#Swords
class swordOfStupidity(baseM.basicSword):
    def __init__(self):
        self.name = "Sword of Stupidity"
        self.desc = "A sword whose power inversely correlates with the intelligence of its wielder"
        self.damage = 0
        
class VBlade(basicSword):
    def __init__(self):
        self.name = "Vorpal Blade"
        self.desc = "A razor-sharp sword, Outlines of strange and terrifying beasts are engraved on the blade."
        self.damage = 15
        
class rustySword(basicSword):
    def __init__(self):
        self.name = "Rusty Sword"
        self.desc = "A rusted, britle sword from a traveler long forgotten..."
        self.damage = 4

class shiv(basicSword):
    def __init__(self):
        self.name = "Shiv"
        self.desc = "Stabby stabby!"
        self.damage = 7

class ghoulClaw(basicSword):
    def __init__(self):
        self.name = "Ghoul Claw"
        self.desc = "It seems ethereal.."
        self.damage = 4
        self.lifesteal = 4 #Not implemented yet!
        
class heavySword(basicSword):
    def __init__(self):
        self.name = "Heavy Sword"
        self.desc = "The heavy, steel sword of an old warrior..."
        self.damage = 35

#Armor/Shields
class frayedCloth(basicDefensiveItem):
    def __init__(self):
        self.name = "Frayed Cloth Armor"
        self.desc = "A frayed, deteriorating cloth..."
        self.block = 4
        
#Magic
