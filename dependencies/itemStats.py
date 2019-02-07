import random

#Basic Item Classes, extend these.
class basicItem():
    def __init__(self):
        self.name = None
        self.desc = ""

    def __str__(self):
        return self.name

    def readDesc(self):
        print(self.desc)
        
    def onFloorClimb(self, player):
        pass

class basicSword(basicItem):
    def __init__(self):
        self.name = "Sword"
        self.desc = "A weapon, I think."
        self.damage = 10
        self.lifesteal = 0

    def boostDamage(self, initial):
        return initial+self.damage

class basicDefensiveItem(basicItem):
    def __init__(self):
        self.name = "Shield"
        self.desc = "Use it"
        self.block = 10
        self.returnDmg = 0
        self.dodge = 0
       
    def boostDefense(self, defense):
        return defense+self.block
    
    def whenAttacked(self, dmg, attacker):
        r = random.randint(1,100)
        if r <= dodge:
            return 0
        else:
            attacker.health -= this.returnDamage
            return dmg-self.block

class basicMagicItem(basicItem):
    # Magic Items should have a function to replace donothing in self.magic. This function will run whenever a player chooses the magic option in a fight
    def donothing():
        pass
    
    def __init__(self):
        self.name = "Magic Item"
        self.desc = "Abracadabra! Use this item in combat for special abilities"
        self.magic = donothing()

class basicPotion(basicItem):
    def drinkPotion():
        pass
    
    def __init__(self):
        self.name = "Basic Potion"
        self.desc = "Drink for special effects"
        self.effect = 
        
#Testing stuff: remove later
class testerSword(basicSword):
    def __init__(self):
        self.name = "Tester Sword"
        self.desc = "Testing testing.."
        self.damage = 1000
        
#Regular Items
class letterFromTheDeceased(basicItem):
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
class swordOfStupidity(basicSword):
    def __init__(self):
        self.name = "Sword of Stupidity"
        self.desc = "A sword whose power inversely correlates with the intelligence of its wielder"
        self.damage = 0
        
class vorpalBlade(basicSword):
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

class peasantsBlade(basicSword):
    def __init__(self):
        self.name = "Peasant Blade"
        self.desc = "Not the most effective weapon, but at least you didn't die"
        self.damage = 2
        
class kingsBlade(basicSword):
    def __init__(self):
        self.name = "King's Blade"
        self.desc = "A valuable sword inlaid with gold and jewels"
        self.damage = 8
        
class herosBlade(basicSword):
    def __init__(self):
        self.name = "Hero's Blade"
        self.desc = "The weapon of a true hero"
        self.damage = 30
        
#Armor/Shields
class loincloth(basicDefensiveItem):
    def __init__(self):
        self.name = "Loincloth"
        self.desc = "It's for public decency"
        self.block = 0

class frayedClothArmor(basicDefensiveItem):
    def __init__(self):
        self.name = "Frayed Cloth Armor"
        self.desc = "A frayed, deteriorating cloth..."
        self.block = 4
        
class steelPlateArmor(basicDefensiveItem):
    def __init__(self):
        self.name = "Steel Plate Armor"
        self.desc = "Strong armor worn by an old warrior"
        self.block = 25
        
class cloak(basicDefensiveItem):
    def __init__(self):
        self.name = "Cloak"
        self.desc = "The cloak of an assassin"
        self.block = 6
        self.dodge = 5
        
#Magic
