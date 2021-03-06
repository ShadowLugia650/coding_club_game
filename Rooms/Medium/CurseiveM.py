import sys, random
sys.path.insert(0, "dependencies")
import baseM, curseScript, itemStats, pScript

def run(player):
    print("You walk into a large room with three doors glowing an ominous dark purple.")
    choice = input("Which door do you choose? [Left, Middle, Right]")
    if choice.title() in ["Left", "L"]:
        print("You open the left door and feel the dark energy surround you.")
        itm = random.choice(player.items)
        eph = curseScript.ephemeral()
        eph.target = itm
        print("Your {} looks empowered by the dark energies, but it also seems to start to fade as you hold it.".format(itm))
        if issubclass(type(itm), itemStats.basicSword):
            itm.damage *= 2
        elif issubclass(type(itm), itemStats.basicDefensiveItem):
            itm.block *= 2
        player.curses.append(eph)
    elif choice.title() in ["Middle", "M"]:
        print("Behind the door lies a tall mound of gold with the same purple glow.")
        print("Filled with greed, you collect up all the gold. However, you begin to feel weak and frail..")
        pScript.earnGold(player, 150)
        player.curses.append(curseScript.exhaustion())
    elif choice.title() in ["Right", "R"]:
        print("As you open the door, the purple gas seeps out and surrounds you. The roomlies empty in front of you..")
        print("You feel confident, as though nothing can stand in your way.")
        player.curses.append(curseScript.hubris())
    else:
        baseM.checkCommands(choice, player)
        run(player)
    return player
