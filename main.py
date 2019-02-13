import sys, random

sys.path.insert(0, 'dependencies')
import console, pScript, baseM, itemStats

sys.path.insert(0, 'Rooms/Easy')
import shopM, battleZombomanM, bestRoomRC, GobolinRC, goldenTreeM
easy= [shopM, battleZombomanM, bestRoomRC, GobolinRC, goldenTreeM]
sys.path.insert(0, 'Rooms/Medium')
import strangerJGv1, battleGhoulM, mirrorsM, lavaroomRCv1, skeletonCalvin
med = [strangerJGv1, battleGhoulM, mirrorsM, lavaroomRCv1, skeletonCalvin]
sys.path.insert(0, 'Rooms/Hard')
import owM, Collector, demonicWarrior
hard= [owM, Collector, demonicWarrior]
sys.path.insert(0, 'Rooms/Impossible')
impossible = []

Player = pScript.PChar()
levels = easy
consol = ""
rounds = 0

baseM.initIntro(Player)
while Player.alive:
    room = levels[random.randint(0, (len(levels)-1))]
    consol = console.getInput(Player, ["yes", "no"], "next room? ")
    if consol.lower() in ["yes", "y", "ok", "sure", "yeah", "yay"]:
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
    if rounds == 3:
        levels += med
    elif rounds == 20:
        levels += hard
print("Game over.")
print("rooms cleared:  " + str(rounds))
print("Ending gold:    " + str(Player.gold))
print("Ending items:")
for i in Player.items:
    print("- {}".format(i))
input()



