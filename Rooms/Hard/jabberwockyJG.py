import sys, random
sys.path.insert(0, 'dependencies')
import baseM, console, pScript
from itemStats import vorpalBlade, jabberwockyHead

class jabberwocky(baseM.basicEnemy):
    def __init__(self):
        self.type = "Jabberwocky"
        self.baseDamage = 89
        self.baseDef = 0
        self.block = 0
        self.health = 1000
        self.maxHp = 1000
        self.loot = [("Gold", random.randint(40,90)),jabberwockyHead()]
        self.options = {"Eviscerate":0}
    
def fight(player, tf, first):
    if tf == True:
        jabber = jabberwocky()
        if first == False:
            print("""As you get nearer to the wabe, The dreadful burbling gets louder and louder...
It's right behind you!
you spin around to find the Jabberwocky blocking your escape!
""")
        else:
            print("You ready your weapons, as the ferocious Jabberwocky bursts from the underbrush.")
        vb = baseM.getItem("Vorpal Blade", player)
        if vb is not None:
            vb.damage = 1000
            print("The Vorpal Blade suddenly hums and glows with energy!")
        baseM.runBasicFight(player, [jabber], 0, first)
        if player.alive:
            print("You hath slain the Jabberwock! O Frabjous Joy! Callooh! Callay!")
        if vb is not None:
            vb.damage = 15
            print("The power dissipates as quickly as it came...")
    else:
        print("You ready your weapons, but nothing came...")

def runAway(player, tf):
    print("You ran away.")
    if len(player.items) > 0:
        lost = random.choice(player.items)
        print("In your haste, you forgot to grab your " + lost.name + "!")
        pScript.removeItem(player, lost)
        goBack(player, tf, lost)

def goBack(player, tf, lost):
    response = console.getInput(player, ["yes","no"],("Go back for " + lost.name + "?"))
    if response == "yes":
        if tf == True:
            fight(player, tf, False)
            if player.alive != True:
                return False
            print("Unfortunately, your " + lost.name + " was lost in the fight.")
        else:
            print("You find your " + lost.name + " peacefully resting at the base of the tree, seemingly mocking your cowardice.")
            pScript.addItem(player, lost)
    else:
        print("You figure it's not worth going back.")

def nap(player, tf):
    if tf == False:
        print("You take a nice, relaxing nap. You awaken feeling refreshed.")
        pScript.heal(player, random.randint(15, 45))
    else:
        print("""You fall asleep as the the incessant burbling drones on in the background.
...
....

You awaken to the feeling of rank, viscous liquid dripping on your face. A sour scent of fermenting flesh fills the air.
Stooping above you, the massive maw of the Jabberwocky foams and drips its prey...


The sounds of your screams and crunching bones reverbrates across the Wabe.
All mimsy were the borogoves,
And the mome raths outgrabe.""")
        player.health = 0
        pScript.checkDeath(player)

def run(player):
    jabTrue = random.choice([True, False])
    print("""At brillig, you see slithy toves
gyring and gimbling in the wabe. 
All mimsy are the borogoves, 
And the mome raths outgrabe. 

You stop in uffish thought under a nearby Jubjub tree.
""")
    print("You hear a faint yet vicious burbling from the bushes beyond the wabe... or is it just your imagination?")
    response = console.getInput(player, ["1","2", "3"],"""What do you do?
[1] prepare to fight
[2] run away
[3] take a nap\n""")
    if response == "1":
        fight(player, jabTrue, True)
        
    elif response == "2":
        runAway(player, jabTrue)

    elif response == "3":
        nap(player, jabTrue)
    return player
