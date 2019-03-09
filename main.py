import sys, random

sys.path.insert(0, 'dependencies')
import console, pScript, baseM, itemStats, curseScript

sys.path.insert(0, 'Rooms/Easy')
import shopM, battleZombomanM, bestRoomRC, GobolinRC, goldenTreeM
easy= [shopM, battleZombomanM, bestRoomRC, GobolinRC, goldenTreeM]
sys.path.insert(0, 'Rooms/Medium')
import strangerJGv1, battleGhoulM, mirrorsM, lavaroomRCv1, skeletonCalvin, reverseRoomAT, jabberwockyJG, randomMediumBattlesM, slimeroomCalvin, CurseiveM, bogGiantRC, ExpensiveRC
med = [strangerJGv1, battleGhoulM, mirrorsM, lavaroomRCv1, skeletonCalvin, reverseRoomAT, jabberwockyJG, CurseiveM, bogGiantRC, ExpensiveRC]
for i in range(3): #increase for each enemy added to randombattles
    med.append(randomMediumBattlesM)
sys.path.insert(0, 'Rooms/Hard')
import owM, Collector, demonicWarrior
hard= [owM, Collector, demonicWarrior]
sys.path.insert(0, 'Rooms/Impossible')
import TimeEater
impossible = [TimeEater]
def game():
    Player = pScript.PChar()
    levels = easy
    consol = ""
    rounds = 0
    lastRoom = None

    baseM.initIntro(Player)
    while Player.alive:
        possibleLevels = levels
        if Player.impossible:
            possibleLevels += impossible
        room = random.choice(possibleLevels)
        while room == lastRoom:
            room = random.choice(possibleLevels)
        lastRoom = room
        consol = console.getInput(Player, ["yes", "y", "ok", "sure", "yeah", "yay", "no", "nay", "n", "nok"], "next room? ")
        if consol.lower() in ["yes", "y", "ok", "sure", "yeah", "yay"]:
            room.run(Player)
            rounds += 1
            Player.timeClimbing += 2
            for i in Player.items:
                try:
                    if issubclass(i, itemStats.basicItem()):
                        i.onFloorClimb(Player)
                except TypeError:
                    pass
            for i in Player.curses:
                try:
                    if issubclass(i, curseScript.basicCurse()):
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
    game()
game()



