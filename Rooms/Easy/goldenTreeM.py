import sys, time
sys.path.insert(0, 'dependencies')
import baseM, pScript, itemStats

def stealLeaves(player):
    print("You pick some leaves and place them into your bag..")
    pScript.earnGold(player, 13)
    chc = input("You feel great, but the other leaves look even more appealing...[Climb, Leave]")
    if chc.title() in ["Climb","C","More","M"]:
        print("You start to climb up the tree, collecting leaves as you go..")
        print("You continue climbing the tree.. As you reach the top, the tree starts to tip.")
        pScript.earnGold(player, 62)
        player.health -= 14
        print("You fall off the tree, taking 14 damage.")
    elif chc.title() in ["Leave", "L"]:
        print("You leave the room with the leaves in your bag.")
        return player
    else:
        baseM.checkCommands(chc, player)
        stealLeaves(player)

def destree(player, timesHit = 0):
    if baseM.hasWeapon(player):
        input("You ready your weapons...")
        if timesHit == 0:
            print("\"CLANG!!!\"")
            choice = input("Leaves start raining down. However, you hear the faint sound of footsteps.. [Hit Again, Collect Leaves, Leave]")
        elif timesHit == 1:
            print("\"CLANG!!\" The shock and recoil from the tree shoots up your arms.")
            choice = input("More leaves rain down. The sound of footsteps grows louder.. [Hit Again, Collect Leaves, Leave]")
        elif timesHit == 2:
            print("\"CLANG!\" More pain shoots up your arms and you stagger back.")
            choice = input("The ground is almost covered in golden leaves. You no longer hear any footsteps. [Hit Again, Collect Leaves, Leave]")
        elif timesHit == 3:
            choice = input("\"CLANG\" You stagger back and fall down. [Hit Again, Collect Leaves, Leave]")
        elif timesHit == 4:
            print("\"clang...\" You feel weak and exhausted. You collapse onto a pile of golden leaves.")
            choice = input("[Collect Leaves, Leave]")
        if choice.title() in ["Hit", "Again", "H", "Hit Again"]:
            timesHit += 1
            destree(player, timesHit)
        elif choice.title() in ["Collect", "Leaves", "C", "Collect Leaves"]:
            input("You quickly gather up all the leaves on the ground and leave the room. [Continue]")
            pScript.earnGold(player, 17*(timesHit+1))
        elif choice.title() in ["Leave", "L"]:
            input("You leave the room wondering how much the golden leaves were really worth. [Continue]")
        else:
            baseM.checkCommands(choice, player)
            destree(player, timesHit)
    else:
        print("You punch the tree as hard as you can. A lone leaf falls down, and your hand hurts.")
        pScript.damage(player, 3)
        print("You pick up the leaf and leave the room.")
        pScript.earnGold(player, 2)
    return player

def waitp3(player):
    ch3 = input('"Hello, traveller. What brings you here today?"["I\'m lost.", "I seek riches.", "I need healing."]')
    if ch3.title() in ["I'm Lost", "Im Lost", "Lost", "I Am Lost"]:
        print("\"Lost, are you? Here..\"")
        pScript.heal(player, 14)
        pScript.addItem(player, itemStats.healthPotion())
        print("The hooded figure points to a large open doorway.")
        print("\"There's the exit. Good luck with your journey.\"")
        input("The hooded figures leave. [Continue]")
    elif ch3.title() in ["I Seek Riches", "Riches", "Gold", "Money"]:
        print("\"Ah.. Riches, yes? Then you've come to the right place..\"")
        print("The hooded figure reaches up and breaks a large branch from the tree.")
        print("He handles it with expertise and carefully places it in your bag.")
        pScript.earnGold(player, 320)
        print("\"You have proven yourself. Continue your adventure.\"")
        #input("As the hooded figures leave, you notice something glimmering in your bag..[Continue]")
        #add some item here.
    elif ch3.title() in ["I Need Healing", "Heal", "Health", "Recover"]:
        print("\"You have taken much damage over your journey so far. Here\"")
        pScript.heal(player, 27)
        if len(player.curses) > 0:
            rm = []
            for curse in player.curses:
                rm.append(curse)
            for curse in rm:
                curse.remove(player)
            print("You feel light and healthy.")
        print("\"The exit is to your right. Good luck on your adventure.\"")
        input("The hooded figures leave. [Continue]")
    else:
        baseM.checkCommands(ch3, player)
        waitp3(player)
    return player

def waitp2(player):
    ch2 = input("Your legs start to grow tired, and you feel as though you've been standing for hours..[Sit Down, Stay Standing]")
    if ch2.title() in ["Sit", "Sit Down", "Down"]:
        print("You sit down by the tree.")
        for i in range(5):
            for j in range(3):
                time.sleep(2)
                print('.',end='')
                player.timeClimbing+=2
            print()
        print("You fall asleep.")
        player.timeClimbing+= 100
        print("You wake up, hearing the murmers of numerous hooded figures standing around you.")
        waitp3(player)
    elif ch2.title() in ["Stand", "Stay", "Stay Standing"]:
        print("You stay standing.")
        for i in range(2):
            for i in range(3):
                time.sleep(2)
                print('.',end='')
                player.timeClimbing+=2
        print("Nothing happens. After waiting for hours, you grow bored and leave.")
    else:
        baseM.checkCommands(ch2, player)
        waitp2(player)
    return player

def wait(player, repeat = False):
    if repeat:
        ch1 = input("Nothing seems to be happening...[Keep Waiting, Leave]")
    else:
        print("You wait. You feel like someone's watching you..")
        for i in range(3):
            time.sleep(2)
            print(".",end="")
            player.timeClimbing+=2
        ch1 = input("Nothing seems to be happening...[Keep Waiting, Leave]")
    if ch1.title() in ["Stay", "Keep", "Wait", "Waiting", "Keep Waiting"]:
        for i in range(3):
            for j in range(3):
                time.sleep(2)
                print(".",end="")
                player.timeClimbing+=2
            print()
        waitp2(player)
    elif ch1.title() in ["Leave","L"]:
        print("You exit the room without a sound.")
    else:
        baseM.checkCommands(ch1, player)
        wait(player, True)
    return player

def run(player):
    print("At the center of the room lies a large golden tree. The branches look sharp and irregular..")
    print("You approach the tree. Your urge to steal the golden leaves is almost irresistible...")
    choice = input("[Steal Leaves, Break Branches, Destroy Tree, Wait, Leave]")
    if choice.title() in ["Steal", "Rob", "Leaves", "Leaf", "S", "Steal Leaves"]:
        stealLeaves(player)
    elif choice.title() in ["Break", "Branches", "Branch", "Brk", "B", "Break Branches"]:
        print("You break off a branch of the tree. It's a lot heavier than you expected, and its irregular, sharp edges cut you.")
        pScript.earnGold(player, 163)
        pScript.damage(player, 30)
    elif choice.title() in ["Destroy", "Tree", "D", "Destroy Tree"]:
        destree(player)
    elif choice.title() in ["Wait", "Stay", "Stand", "W"]:
        wait(player)
    elif choice.title() in ["Leave", "L"]:
        input("You leave the room, not wanting to be greedy. [Continue]")
    else:
        baseM.checkCommands(choice, player)
        run(player)
    return player
