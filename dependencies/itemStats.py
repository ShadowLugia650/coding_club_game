import random, baseM

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
        self.name = "Basic Sword"
        self.desc = "A weapon, I think."
        self.damage = 0
        self.lifesteal = 0

    def boostDamage(self, initial):
        return initial+self.damage

class basicDefensiveItem(basicItem):
    def __init__(self):
        self.name = "Basic Defensive Item"
        self.desc = "Use it"
        self.block = 0
        self.returnDmg = 0
        self.dodge = 0
       
    def boostDefense(self, defense):
        return defense+self.block
    
    def whenAttacked(self, dmg, attacker):
        try:
            if random.randint(1,100) <= self.dodge:
                return 0
        except AttributeError:
            pass
        try:
            attacker.health -= self.returnDamage
        except AttributeError:
            pass
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
    def drinkPotion(self, player):
        pass
    
    def __init__(self):
        self.name = "Basic Potion"
        self.desc = "Drink for special effects"
        
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

class jabberwockyHead(basicItem):
    def __init__(self):
        self.name = "Jabberwocky Head"
        self.desc = "The severed head of the Jabberwocky. Despite being dead, its eyes seem to follow you with malicious hunger."
        
class corruptBlood(basicItem):
    def __init__(self):
        self.name = "Corrupt Blood"
        self.desc = "A strange bluish-purple liquid..."

    def onFloorClimb(self, player):
        player.health += 10

class wornJournal(basicItem):
    def __init__(self):
        self.name = "Worn Journal"
        self.desc = "An old, worn out journal. The pages are dusty and faded.."
        
    def read(self):
        #implement this
        pass
        
#Swords
class sword(basicSword):
    def __init__(self):
        self.name = "Sword"
        self.desc = "It deals damage. Use it!"
        self.damage = 10
    
class swordOfStupidity(basicSword):
    def __init__(self):
        self.name = "Sword of Stupidity"
        self.desc = "A sword whose power inversely correlates with the intelligence of its wielder"
        self.damage = 0
        
class vorpalBlade(basicSword):
    def __init__(self):
        self.name = "Vorpal Blade"
        self.desc = "A razor-sharp sword. Outlines of strange and terrifying beasts are engraved on the blade."
        self.damage = 15
        
class rustySword(basicSword):
    def __init__(self):
        self.name = "Rusty Sword"
        self.desc = "A rusted, brittle sword from a traveler long forgotten..."
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
        
class demonicSword(basicSword):
    def __init__(self):
        self.name = "Demonic Blade"
        self.desc = "A sword infused with demonic energy"
        self.damage = 10
        
    def boostDamage(self, initial):
        self.damage += 3
        return initial+self.damage
        
#Armor/Shields
class shield(basicDefensiveItem):
    def __init__(self):
        self.name = "Shield"
        self.desc = "You should probably use this."
        self.block = 10

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
        
class glowingEyes(basicDefensiveItem):
    def __init__(self):
        self.name = "Glowing Eyes"
        self.desc = "A large stone statue with red glowing eyes."
        self.block = 12
        
#Magic
class wandOfConfusion(basicMagicItem):
    def __init__ (self):
        self.name="Wand of Confusion"
        self.desc="Bamboozles, hoodwinks, leads astray, runs amok, and flat out decieves your enemies"
    def magic(self, player, enemy):
        enemy.baseDamage=random.randint(0,enemy.baseDamage)
        
        
        
class staffOfGold(basicMagicItem):
    def magic(self,player,enemy):
        if self.charge==0:
            player.gold+=10
        player.gold+=self.charge
        self.charge-=10
    def __init__ (self):
        self.name="Staff of Gold"
        self.desc=""
        self.charge=150
        
class orbOfThunder(basicMagicItem):
    def magic(self, player, enemy):
        enemy.health -= 8
        
    def __init__(self):
        self.name = "Orb of Thunder"
        self.desc = "It's an orb. And it zaps people with lightning. But thunder sounded better for the name, so that's what we went with."

class orbOfVampirism(basicMagicItem):
    def magic(self, player, enemy):
        enemy.health -= 6
        player.health += 6

    def __init__(self):
        self.name = "Orb of Vampirism"
        self.desc = "A curious, swirling, dark-purple orb. It seems to radiate dark energy."
        
class staffOfLuck(basicMagicItem):
    def __init__ (self):
        self.name="Staff of Luck"
        self.desc="Test your luck"
        self.count=4
    def magic(self,player,enemy):
        if self.count==0:
            self.count=4
            print("Sorry! The lucky number was "+str(luckynumber))
            return
        elif self.count==4:
            luckynumber=random.randint(1,20)
        print("As you hold up the worn staff, you realize that a bit of luck may be required to make it work")
        print("guess a number from 1 to 20")
        guess=input()
        if luckynumber==int(guess):
            print("Fueled by your luck, a bolt of lightning strikes the "+enemy.name)
            if count==4:
                enemy.health=0
            enemy.health-=(0.5*enemy.health)
            self.count=4
        elif int(guess)<luckynumber:
            print("Oops! You guessed too low!")
            self.count-=1
            print ("You have "+str(count)+"guesses left!")
            self.magic(self,player,enemy)
        elif int(guess)>luckynumber:
            print("Oops! You guessed too high!")
            self.count-=1
            print ("You have "+str(count)+"guesses left!")
            self.magic(self,player,enemy)
            
class amplifyingOrb(basicMagicItem):
    def __init__(self):
        self.name = "Amplifying Orb"
        self.desc = "Amplifies your attacks with the Demonic Blade"
    
    def magic(self,player,enemy):
        db = baseM.getItem("Demonic Blade", player)
        db.damage *= 2
        print("The demonic energies swirl around your Demonic Blade! It doubles in strength! ({})".format(db.damage))
        
class epiTome(basicMagicItem):
    def __init__(self):
        self.name = "Epi Tome"
        self.desc = "The Epitome of Magical Abilities in a Tome."
        self.damage = 35
    
    def magic(self,player,enemy):
        enemy.health -= self.damage
        player.health += self.damage
        
#Potions
class healthPotion(basicPotion):
    def drinkPotion(self, player):
        player.health += 10
        
    def __init__(self):
        self.name = "Health Potion"
        self.desc = "It heals you.. supposedly"
