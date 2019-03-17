def game(mode = "Text"):
    import sys, random, copy

    sys.path.insert(0, 'dependencies')
    import console, pScript, baseM, itemStats, curseScript, artAssetsM

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
    player = pScript.PChar()
    levels = easy
    consol = ""
    rounds = 0
    lastRoom = None
    screen = None
    if mode == "Pygame":
        screen = artAssetsM.initScreen()

    baseM.initIntro(player, screen)
    while player.alive:
        torchExists = False
        possibleLevels = copy.copy(levels)
        if player.impossible:
            possibleLevels += impossible
        for itm in player.items:
            if itm.name == "Zomboman Guts":
                possibleLevels.append(battleZombomanM)
            if itm.name =="Torch":
                torchExists = True
        if not torchExists:
            if random.randint(0,10)>6:
                baseM.showText(player, "You tripped in the dark and took 5 damage",screen)
                player.health-=5
        if rounds == 3:
            room = shopM
        else:
            room = random.choice(possibleLevels)
            while room == lastRoom:
                room = random.choice(possibleLevels)
        lastRoom = room
        if player.alive == False:
            baseM.showText(player, "You have died.",screen)
        while True:
            consol = baseM.showText(player, "Next Room? [yes, no]",screen)#console.getInput(player, ["yes", "y", "ok", "sure", "yeah", "yay", "no", "nay", "n", "nok"], "next room? ",screen)
            if consol.lower() in ["yes", "y", "ok", "sure", "yeah", "yay"]:
                room.run(player, screen)
                rounds += 1
                player.timeClimbing += 5
                for i in player.items:
                    try:
                        if issubclass(type(i), itemStats.basicItem):
                            i.onFloorClimb(player, screen)
                    except TypeError:
                        pass
                for i in player.curses:
                    if issubclass(type(i), curseScript.basicCurse):
                        i.onFloorClimb(player, screen)
                break
            elif consol.lower() in ["no", "n", "nok", "not sure", "neah", "nay"]:
                player.alive = False
                break
            else:
                baseM.checkCommands(consol, player, screen)
        if rounds == 5:
            levels += med
        elif rounds == 20:
            levels += hard
    baseM.showText(player, "Game over.",screen)
    baseM.showText(player, "rooms cleared:  " + str(rounds),screen)
    baseM.showText(player, "Ending gold:    " + str(player.gold),screen)
    baseM.showText(player, "Ending items:",screen)
    for i in player.items:
        baseM.showText(player, "- {}".format(i),screen)
    baseM.showText(player, "Your final score is: {}".format(baseM.calculateFinalScore(player,rounds)),screen)
    input()
    levels=easy
    game(mode)
if __name__ == "__main__":
    game()































