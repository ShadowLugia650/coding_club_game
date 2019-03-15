import sys, random, copy

sys.path.insert(0, 'dependencies')
import console, pScript, baseM, itemStats, curseScript

sys.path.insert(0, 'Rooms/Easy')
import shopM, battleZombomanM, bestRoomRC, GobolinRC, goldenTreeM, Armory, trophyRoom
easy= [shopM, battleZombomanM, bestRoomRC, GobolinRC, goldenTreeM, Armory, trophyRoom]
sys.path.insert(0, 'Rooms/Medium')
import strangerJGv1, battleGhoulM, mirrorsM, lavaroomRCv1, skeletonCalvin, reverseRoomAT,  randomMediumBattlesM, slimeroomCalvin, CurseiveM, bogGiantRC, ExpensiveRC, mossyGooberM, ohgur
med = [strangerJGv1, battleGhoulM, mirrorsM, lavaroomRCv1, skeletonCalvin, reverseRoomAT, slimeroomCalvin, CurseiveM, bogGiantRC, ExpensiveRC, mossyGooberM, ohgur]
for i in range(3): #increase for each enemy added to randombattles
    med.append(randomMediumBattlesM)
sys.path.insert(0, 'Rooms/Hard')
import owM, Collector, demonicWarrior, jabberwockyJG
hard= [owM, Collector, demonicWarrior, jabberwockyJG]
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
        possibleLevels = copy.copy(levels)
        if Player.impossible:
            possibleLevels += impossible
        for itm in Player.items:
            if itm.name == "Zomboman Guts":
                possibleLevels.append(battleZombomanM)
        if not itemStats.torch() in Player.items:
            if random.randint(0,10)>6:
                print("You tripped in the dark and took 5 damage")
                player.health-=5
        if rounds == 3:
            room = shopM
        else:
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
                    if issubclass(type(i), itemStats.basicItem):
                        i.onFloorClimb(Player)
                except TypeError:
                    pass
            for i in Player.curses:
                if issubclass(type(i), curseScript.basicCurse):
                    i.onFloorClimb(Player)
        else:
            break
        if Player.alive == False:
            print("You have died.")
        if rounds == 5:
            levels += med
        elif rounds == 20:
            levels += hard
    print("Game over.")
    print("rooms cleared:  " + str(rounds))
    print("Ending gold:    " + str(Player.gold))
    print("Ending items:")
    for i in Player.items:
        print("- {}".format(i))
    print("Your final score is: {}".format(baseM.calculateFinalScore(Player,rounds)))
    input()
    levels=easy
    game()
game()



