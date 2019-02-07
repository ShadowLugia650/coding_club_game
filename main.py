import sys, random

sys.path.insert(0, 'dependencies')
import console, pScript, baseM, itemStats

sys.path.insert(0, 'Rooms/Easy')
sys.path.insert(0, 'Rooms/Medium')
sys.path.insert(0, 'Rooms/Hard')
sys.path.insert(0, 'Rooms/Impossible')
import strangerJGv1, battleGhoulM, mirrorsM, owM, shopM, battleZombomanM, lavaroomRCv1, skeletonCalvin, Collector

Player = pScript.PChar()
levels = [strangerJGv1, battleGhoulM, mirrorsM, owM, shopM, battleZombomanM, lavaroomRCv1, skeletonCalvin, Collector]


#levels = [strangerJGv1, battleGhoulM]
#Why did you switch it to this?

#{strangerJGv1 : 2, battleGhoulM : 5, mirrorsM : 1, owM : 2, shopM : 5} 
consol = ""
rounds = 0

baseM.initIntro(Player)

while Player.alive:
    room = levels[random.randint(0, (len(levels)-1))]
    consol = console.getInput(Player, ["yes", "no"], "next room? ")
    if consol == "yes":
        room.run(Player)
        rounds += 1
        for i in Player.items:
            try:
                if issubclass(i, itemStats.basicItem()):
                    i.onFloorClimb(Player)
            except TypeError:
                pass
    else:
        break
    if Player.alive == False:
        print("You have died.")
    
print("Game over.")
print("rooms cleared:  " + str(rounds))
print("Ending gold:    " + str(Player.gold))
print("Ending items:")
for i in Player.items:
    print("- {}".format(i))
input()



