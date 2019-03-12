import random, baseM

#Basic Item Classes, extend these.
class basicItem():
    def __init__(self):
        self.name = None
        self.desc = ""
        self.value = 0

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
        self.value = 0

    def boostDamage(self, initial):
        return initial+self.damage

class basicDefensiveItem(basicItem):
    def __init__(self):
        self.name = "Basic Defensive Item"
        self.desc = "Use it"
        self.block = 0
        self.returnDmg = 0
        self.dodge = 0
        self.value = 0
       
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
        return dmg

class basicMagicItem(basicItem):
    # Magic Items should have a function called magic(). This function will run whenever a player chooses the magic option in a fight
    def magic(self, player, enemy):
        pass
    
    def __init__(self):
        self.name = "Magic Item"
        self.desc = "Abracadabra! Use this item in combat for special abilities"
        self.value = 0

class basicPotion(basicItem):
    def drinkPotion(self, player):
        pass
    
    def __init__(self):
        self.name = "Basic Potion"
        self.desc = "Drink for special effects"
        self.value = 0
        
#Testing stuff: remove later
class testerSword(basicSword):
    def __init__(self):
        self.name = "Tester Sword"
        self.desc = "Testing testing.."
        self.damage = 1000
        self.value = 0
        
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
        self.value = 3

class jabberwockyHead(basicItem):
    def __init__(self):
        self.name = "Jabberwocky Head"
        self.desc = "The severed head of the Jabberwocky. Despite being dead, its eyes seem to follow you with malicious hunger."
        self.value = 796
        
class corruptBlood(basicItem):
    def __init__(self):
        self.name = "Corrupt Blood"
        self.desc = "A strange bluish-purple liquid..."
        self.value = 6686

    def onFloorClimb(self, player):
        player.health += 10

class wornJournal(basicItem):
    def __init__(self):
        self.name = "Worn Journal"
        self.desc = "An old, worn out journal. The pages are dusty and faded.."
        self.value = 8
        
    def read(self):
        #implement this
        pass
        
class zombomanGuts(basicItem):
    def __init__(self):
        self.name = "Zomboman Guts"
        self.desc = "They have a very strong, horrible smell.."
        self.value = -10
        
#Swords
class sword(basicSword):
    def __init__(self):
        self.name = "Sword"
        self.desc = "It deals damage. Use it!"
        self.damage = 10
        self.value = 100
    
class swordOfStupidity(basicSword):
    def __init__(self):
        self.name = "Sword of Stupidity"
        self.desc = "A sword whose power inversely correlates with the intelligence of its wielder"
        self.damage = 0
        self.value = 93
        
class vorpalBlade(basicSword):
    def __init__(self):
        self.name = "Vorpal Blade"
        self.desc = "A razor-sharp sword. Outlines of strange and terrifying beasts are engraved on the blade."
        self.damage = 15
        self.value = 96
        
class rustySword(basicSword):
    def __init__(self):
        self.name = "Rusty Sword"
        self.desc = "A rusted, brittle sword from a traveler long forgotten..."
        self.damage = 4
        self.value = 0
        
class brokenSword(basicSword):
    def __init__(self):
        self.name = "Broken Sword"
        self.desc = "A broken sword abandoned in an old storage shed"
        self.damage = 2
        self.value = 8
        
class dullKnife(basicSword):
    def __init__(self):
        self.name = "Dull Knife"
        self.desc = "A dull knife abandoned in an old storage shed"
        self.damage = 1
        self.value = 5
        
class rustyPitchfork(basicSword):
    def __init__(self):
        self.name = "Rusty Pitchfork"
        self.desc = "A rusty pitchfork abandoned in an old storage shed"
        self.damage = 3
        self.value = 10
        
class baseballBat(basicSword):
    def __init__(self):
        self.name = "Baseball Bat"
        self.desc = "Maybe you can club some poor Zombo-man with it"
        self.damage = 2
        self.value = 25
        
class shovel(basicSword):
    def __init__(self):
        self.name = "Shovel"
        self.desc = "Shovel Knight is a 2D side-scrolling platform game developed and published by Yacht Club Games."
        self.damage = 2
        self.value = 15
        
class abandonedAxe(basicSword):
    def __init__(self):
        self.name = "Abandoned Axe"
        self.desc = "Some adventurer left this behind, but it's still sharp."
        self.damage = 15
        self.value = 40

class diamondSword(basicSword):
    def __init__(self):
        self.name = "Diamond Sword"
        self.desc = "Who makes a sword out of diamonds?"
        self.damage = 2
        self.value = 1000
        
class warhammer(basicSword):
    def __init__(self):
        self.name = "Warhammer"
        self.desc = "ow"
        self.damage = 10
        self.value = 40
        
class shiv(basicSword):
    def __init__(self):
        self.name = "Shiv"
        self.desc = "Stabby stabby!"
        self.damage = 7
        self.value = 87

class ghoulClaw(basicSword):
    def __init__(self):
        self.name = "Ghoul Claw"
        self.desc = "It seems ethereal.."
        self.damage = 4
        self.lifesteal = 3 
        self.value = 23
        
class heavySword(basicSword):
    def __init__(self):
        self.name = "Heavy Sword"
        self.desc = "The heavy, steel sword of an old warrior..."
        self.damage = 35
        self.value = 173

class glowingSword(basicSword):
    def __init__(self):
        self.name = "Glowing Sword"
        self.desc = "The blade glows and seems indestructible"
        self.damage = 13
        self.value = 177
        
class peasantsBlade(basicSword):
    def __init__(self):
        self.name = "Peasant's Blade"
        self.desc = "Not the most effective weapon, but at least you didn't die"
        self.damage = 2
        self.value = 5
        
class kingsBlade(basicSword):
    def __init__(self):
        self.name = "King's Blade"
        self.desc = "A valuable sword inlaid with gold and jewels"
        self.damage = 8
        self.value = 1000
        
class herosBlade(basicSword):
    def __init__(self):
        self.name = "Hero's Blade"
        self.desc = "The weapon of a true hero"
        self.damage = 40
        self.value = 2500
        
class demonicSword(basicSword):
    def __init__(self):
        self.name = "Demonic Blade"
        self.desc = "A sword infused with demonic energy"
        self.trueDesc = "Damage increases by 3 each turn starting at 10."
        self.damage = 10
        self.value = 1900
        
    def boostDamage(self, initial):
        self.damage += 3
        return initial+self.damage
    
class vileBlade(basicSword):
    def __init__(self):
        self.name = "Vile Blade"
        self.desc = "An ancient weapon with a dark past"
        self.damage = 20
        self.value = 76
        
class hungryClock(basicItem):
    def __init__(self):
        self.name = "Hungry Clock"
        self.desc = "A rare relic from the Time Eater. You feel powerful just holding it, but it seems to gnaw at your arm..."
        self.trueDesc = "Attacks deal 33% more damage. Take 4 damage each time you climb a floor."
        self.value = 1234567
        
    def onFloorClimb(self, player):
        player.health -= 4
        
    def boostDamage(self, initial):
        return round(initial*1.33)
        
#Armor/Shields
class shield(basicDefensiveItem):
    def __init__(self):
        self.name = "Shield"
        self.desc = "You should probably use this."
        self.block = 10
        self.value = 100

class loincloth(basicDefensiveItem):
    def __init__(self):
        self.name = "Loincloth"
        self.desc = "It's for public decency"
        self.block = 0
        self.value = 0

class frayedClothArmor(basicDefensiveItem):
    def __init__(self):
        self.name = "Frayed Cloth Armor"
        self.desc = "A frayed, deteriorating cloth..."
        self.block = 4
        self.value = 1
        
class steelPlateArmor(basicDefensiveItem):
    def __init__(self):
        self.name = "Steel Plate Armor"
        self.desc = "Strong armor worn by an old warrior"
        self.block = 25
        self.value = 160
        
class cloak(basicDefensiveItem):
    def __init__(self):
        self.name = "Cloak"
        self.desc = "The cloak of an assassin"
        self.block = 6
        self.dodge = 5
        self.value = 82
        
class armoredShirt(basicDefensiveItem):
    def __init__(self):
        self.name = "Armored Shirt"
        self.desc = "shirt with armor"
        self.block = 10
        self.value = 73
        
class glowingEyes(basicDefensiveItem):
    def __init__(self):
        self.name = "Glowing Eyes"
        self.desc = "A large stone statue with red glowing eyes."
        self.block = 12
        self.value = 241
        
class glowingShield(basicDefensiveItem):
    def __init__(self):
        self.name = "Glowing Shield"
        self.desc = "The shield glows and seems indestructible"
        self.block = 13
        self.value = 177
        
#Magic
class wandOfConfusion(basicMagicItem):
    def __init__ (self):
        self.name="Wand of Confusion"
        self.desc="Bamboozles, hoodwinks, leads astray, runs amok, and flat out decieves your enemies"
        self.value = random.randint(0, 100)
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
        self.value = 300
        
class orbOfThunder(basicMagicItem):
    def magic(self, player, enemy):
        enemy.takeDamage(8, player)
        
    def __init__(self):
        self.name = "Orb of Thunder"
        self.desc = "It's an orb. And it zaps people with lightning. But thunder sounded better for the name, so that's what we went with."
        self.value = 43

class orbOfVampirism(basicMagicItem):
    def magic(self, player, enemy):
        enemy.health -= 6
        player.health += 6

    def __init__(self):
        self.name = "Orb of Vampirism"
        self.desc = "A curious, swirling, dark-purple orb. It seems to radiate dark energy."
        self.value = 85
        
class staffOfLuck(basicMagicItem):
    def __init__ (self):
        self.name="Staff of Luck"
        self.desc="Test your luck"
        self.count=4
        self.value = 72
        
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
            print("Fueled by your luck, a bolt of lightning strikes the "+enemy.type)
            if self.count==4:
                enemy.health=0
            else:
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
            
class glowingOrb(basicMagicItem):
    def magic(self, player, enemy):
        enemy.takeDamage(self.damage)
    
    def __init__(self):
        self.name = "Glowing Orb"
        self.desc = "The staff glows and seems indestructible"
        self.damage = 30
        self.value = 177
            
class amplifyingOrb(basicMagicItem):
    def __init__(self):
        self.name = "Amplifying Orb"
        self.desc = "Amplifies your attacks with the Demonic Blade"
        self.value = 126
    
    def magic(self,player,enemy):
        db = baseM.getItem("Demonic Blade", player)
        db.damage *= 2
        print("The demonic energies swirl around your Demonic Blade! It doubles in strength! ({})".format(db.damage))
        
class epiTome(basicMagicItem):
    def __init__(self):
        self.name = "Epi Tome"
        self.desc = "The Epitome of Magical Abilities in a Tome."
        self.damage = 75
        self.value = 620
    
    def calcDamage(self, player):
        self.damage = 75
        for i in player.items:
            if issubclass(type(i), basicMagicItem):
                self.damage += 15
    
    def onFloorClimb(self, player):
        self.calcDamage(self, player)
    
    def magic(self,player,enemy):
        enemy.health -= self.damage
        player.health += self.damage
        
#Potions
class healthPotion(basicPotion):
    def drinkPotion(self, player):
        player.health += 10
        if player.health > player.maxHp:
            player.health = player.maxHp
        print("You restored 10 health!")
        
    def __init__(self):
        self.name = "Health Potion"
        self.desc = "It heals you.. supposedly"
        self.value = 40

class antidote(basicPotion):
    #should the antidote cure all poisoning or just one instance?
    import curseScript
    def drinkPotion(self, player):
        for i in player.curses:
            if type(i) == curseScript.toxins:
                i.remove(player)
                print("The antidote cured some of your poisoning!")
                return
        print("The antidote had no effect.")
        
    def __init__(self):
        self.name = "Antidote"
        self.desc = "You're told it can cure poisoning..."
        self.value = 80

class ohgurGuts(basicPotion):
    def drinkPotion(self, player):
        player.health += 15
        if player.health > player.maxHp:
            player.health = player.maxHp
        print("You restored 15 health!")
        
    def __init__(self):
        self.name = "Ohgur Guts"
        self.desc = "Ew! Slimy ohgur guts. Maybe they can heal you..."
        self.value = 53
