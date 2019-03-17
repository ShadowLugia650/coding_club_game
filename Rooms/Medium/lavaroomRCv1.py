import sys, random
sys.path.insert(0, "dependencies")
import console, pScript, baseM, itemStats

stupidswordvar = 0
lavadamage = 1
#main room function
def run(player, screen):
    syord = itemStats.swordOfStupidity()
    global stupidswordvar, lavadamage
    print ("""As you enter the room, you feel hot air singe your eyebrows.
You find yourself in a vast cavern split by a river of lava.
A bridge of polished black stone stretches over the lava, and through the smoke you can barely see a door on the far side of the chamber.
Looking around the walls of the cavern, you see a strange, temple-like structure to the left, but it looks dangerously close to the lava.
How would you wish to proceed?
Press 1 to cross the bridge
Press 2 to approach the shrine
Press 3 to cower away from the heat""")
    while True:
        response = console.getInput(player, ["1", "2","3"], "Make your choice")
        if response.lower() == "1":
            crossbridge(player, screen)
            lavadamage=1   
            return player
        if response.lower() == "2":
            shrine(player, syord)
            lavadamage=1
            return player
        if response.lower() =="3":
            vegetate(player, screen)
            
        
#the idea of this room is that the longer you stay, the more damage you will take from the heat of the lava. But the more damage you take from the lava, the stronger your reward will be

#path 1-BORING
def crossbridge(player, screen):
    global stupidswordvar, lavadamage
    print ("""You carefully make your way across the bridge.
Despite the spiderweb cracks in its base, the bridge seems to be holding up fine.
Being this close to the lava is taking its toll on you, though. You take """+str(lavadamage)+" damage")
    pScript.damage(player,lavadamage)
    lavadamage+=1

#path 2-the good one    
def shrine(player, swordOfStupidity):
    global stupidswordvar, lavadamage
    print ("""The shrine is on the far side of the cavern, and it feels like hours as you slog through the blistering heat.
You take """+str(lavadamage)+" damage from the heat")
    pScript.damage(player,lavadamage)
    lavadamage+=1
    print ("""You look back at the bridge. It still seems close enough to cross easily, and it's only getting hotter as you near the shrine.
Will you turn back?
Press 1 to continue to the shrine
Press 2 to turn back and cross the bridge""")
    while True:
        response1 = console.getInput(player, ["1", "2"], "Make your choice")
        if response1.lower() == "1":
            print ("As you approach the shrine,you notice that it appears to have been chiseled out of a solid block of obsidian.")
            print ("A huge sword is planted in the otherwise smooth obsidian near the edge of the lava.")
            print ("Since the entire shrine is made out of black rock, it radiates intense heat as you approach.")
            print ("Or maybe it's just because you're so close to the lava. Regardless, you take "+str(lavadamage)+" damage from the heat")
            pScript.damage(player,lavadamage)
            lavadamage+=1
            print ("As you stumble toward the shrine, you see an opening in the cavern wall behind it. Safety!")
            print ("But then you hesitate, looking back at the unclaimed sword. It would be a shame to just leave it there...")
            print ("Press 1 to go back for the sword")
            print ("Press 2 to head for the exit")
            while True:
                response2 = console.getInput(player, ["1", "2"], "Make your choice")
                if response2.lower() == "1":
                    print ("Feeling the heat of the lava singeing your hair and eyes, you stagger up to the sword")
                    print ("Etched into the glassy stone reads the inscription: SWORD OF STUPIDITY-A WEAPON TO EMPOWER THE IRRATIONAL AND FOOLHARDY")
                    print ("You yank the sword from its stone sheath and instantly feel the heat drain from your body into the sword.")
                    pScript.addItem(player,swordOfStupidity)
                    stupidswordvar = 3*lavadamage
                    swordOfStupidity.damage = stupidswordvar
                    print ("Your Sword of stupidity has "+str(swordOfStupidity.damage)+" strength")
                    #Sword of Stupidity is meant to increase your attack damage by the value of stupidswordvar
                    print ("Feeling empowered, you stride confidently to the exit")
                    return player
                if response2.lower() == "2":
                    print ("You stagger into the blessedly cool tunnel, and continue on your way without looking back.")
                    return player
        if response1.lower() == "2":
            crossbridge(player, screen)   
            return player

#path 3-transcendent    
def vegetate(player, screen):
    global stupidswordvar, lavadamage
    print ("""The heat of the lava is overpowering, and going closer to the bridge or the shrine would probably roast you alive.
Unfortunately, it's not much better where you're standing. You take """+str(lavadamage)+" damage from the lava's heat")
    pScript.damage(player,lavadamage)
    lavadamage+=1
    baseM.showText(player, """You reconsider your options. Both the shrine and the bridge still seem extremely unnappealing
How would you wish to proceed?
Press 1 to cross the bridge
Press 2 to approach the shrine
Press 3 to cower away from the heat""")

















