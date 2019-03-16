import sys, time
sys.path.insert(0, 'dependencies')
import baseM, pScript, itemStats

def stealLeaves(player, screen):
    baseM.showText("You pick some leaves and place them into your bag..",screen)
    pScript.earnGold(player, 13)
    chc = baseM.showText("You feel great, but the other leaves look even more appealing...[Climb, Leave]",screen)
    if chc.title() in ["Climb","C","More","M"]:
        baseM.showText("You start to climb up the tree, collecting leaves as you go..",screen)
        baseM.showText("You continue climbing the tree.. As you reach the top, the tree starts to tip.",screen)
        pScript.earnGold(player, 62)
        player.health -= 14
        baseM.showText("You fall off the tree, taking 14 damage.",screen)
    elif chc.title() in ["Leave", "L"]:
        baseM.showText("You leave the room with the leaves in your bag.",screen)
        return player
    else:
        baseM.checkCommands(chc, player)
        stealLeaves(player, screen)

def destree(player, timesHit = 0):
    if baseM.hasWeapon(player, screen):
        baseM.showText("You ready your weapons...",screen)
        if timesHit == 0:
            baseM.showText("\"CLANG!!!\"",screen)
            choice = baseM.showText("Leaves start raining down. However, you hear the faint sound of footsteps.. [Hit Again, Collect Leaves, Leave]",screen)
        elif timesHit == 1:
            baseM.showText("\"CLANG!!\" The shock and recoil from the tree shoots up your arms.",screen)
            choice = baseM.showText("More leaves rain down. The sound of footsteps grows louder.. [Hit Again, Collect Leaves, Leave]",screen)
        elif timesHit == 2:
            baseM.showText("\"CLANG!\" More pain shoots up your arms and you stagger back.",screen)
            choice = baseM.showText("The ground is almost covered in golden leaves. You no longer hear any footsteps. [Hit Again, Collect Leaves, Leave]",screen)
        elif timesHit == 3:
            choice = baseM.showText("\"CLANG\" You stagger back and fall down. [Hit Again, Collect Leaves, Leave]",screen)
        elif timesHit == 4:
            baseM.showText("\"clang...\" You feel weak and exhausted. You collapse onto a pile of golden leaves.",screen)
            choice = baseM.showText("[Collect Leaves, Leave]",screen)
        if choice.title() in ["Hit", "Again", "H", "Hit Again"]:
            timesHit += 1
            destree(player, timesHit)
        elif choice.title() in ["Collect", "Leaves", "C", "Collect Leaves"]:
            baseM.showText("You quickly gather up all the leaves on the ground and leave the room. [Continue]",screen)
            pScript.earnGold(player, 17*(timesHit+1))
        elif choice.title() in ["Leave", "L"]:
            baseM.showText("You leave the room wondering how much the golden leaves were really worth. [Continue]",screen)
        else:
            baseM.checkCommands(choice, player)
            destree(player, timesHit)
    else:
        baseM.showText("You punch the tree as hard as you can. A lone leaf falls down, and your hand hurts.",screen)
        pScript.damage(player, 3)
        baseM.showText("You pick up the leaf and leave the room.",screen)
        pScript.earnGold(player, 2)
    return player

def waitp3(player, screen):
    ch3 = baseM.showText('"Hello, traveller. What brings you here today?"["I\'m lost.", "I seek riches.", "I need healing."]',screen)
    if ch3.title() in ["I'm Lost", "Im Lost", "Lost", "I Am Lost"]:
        baseM.showText("\"Lost, are you? Here..\"",screen)
        pScript.heal(player, 14)
        pScript.addItem(player, itemStats.healthPotion())
        baseM.showText("The hooded figure points to a large open doorway.",screen)
        baseM.showText("\"There's the exit. Good luck with your journey.\"",screen)
        baseM.showText("The hooded figures leave. [Continue]",screen)
    elif ch3.title() in ["I Seek Riches", "Riches", "Gold", "Money"]:
        baseM.showText("\"Ah.. Riches, yes? Then you've come to the right place..\"",screen)
        baseM.showText("The hooded figure reaches up and breaks a large branch from the tree.",screen)
        baseM.showText("He handles it with expertise and carefully places it in your bag.",screen)
        pScript.earnGold(player, 320)
        baseM.showText("\"You have proven yourself. Continue your adventure.\"",screen)
        #baseM.showText("As the hooded figures leave, you notice something glimmering in your bag..[Continue]",screen)
        #add some item here.
    elif ch3.title() in ["I Need Healing", "Heal", "Health", "Recover"]:
        baseM.showText("\"You have taken much damage over your journey so far. Here\"",screen)
        pScript.heal(player, 27)
        if len(player.curses) > 0:
            rm = []
            for curse in player.curses:
                rm.append(curse)
            for curse in rm:
                curse.remove(player, screen)
            baseM.showText("You feel light and healthy.",screen)
        baseM.showText("\"The exit is to your right. Good luck on your adventure.\"",screen)
        baseM.showText("The hooded figures leave. [Continue]",screen)
    else:
        baseM.checkCommands(ch3, player)
        waitp3(player, screen)
    return player

def waitp2(player, screen):
    ch2 = baseM.showText("Your legs start to grow tired, and you feel as though you've been standing for hours..[Sit Down, Stay Standing]",screen)
    if ch2.title() in ["Sit", "Sit Down", "Down"]:
        baseM.showText("You sit down by the tree.",screen)
        for i in range(5):
            for j in range(3):
                time.sleep(2)
                baseM.showText('.',end='',screen)
                player.timeClimbing+=2
            baseM.showText(,screen)
        baseM.showText("You fall asleep.",screen)
        player.timeClimbing+= 100
        baseM.showText("You wake up, hearing the murmers of numerous hooded figures standing around you.",screen)
        waitp3(player, screen)
    elif ch2.title() in ["Stand", "Stay", "Stay Standing"]:
        baseM.showText("You stay standing.",screen)
        for i in range(2):
            for i in range(3):
                time.sleep(2)
                baseM.showText('.',end='',screen)
                player.timeClimbing+=2
        baseM.showText("Nothing happens. After waiting for hours, you grow bored and leave.",screen)
    else:
        baseM.checkCommands(ch2, player)
        waitp2(player, screen)
    return player

def wait(player, repeat = False):
    if repeat:
        ch1 = baseM.showText("Nothing seems to be happening...[Keep Waiting, Leave]",screen)
    else:
        baseM.showText("You wait. You feel like someone's watching you..",screen)
        for i in range(3):
            time.sleep(2)
            baseM.showText(".",end="",screen)
            player.timeClimbing+=2
        ch1 = baseM.showText("Nothing seems to be happening...[Keep Waiting, Leave]",screen)
    if ch1.title() in ["Stay", "Keep", "Wait", "Waiting", "Keep Waiting"]:
        for i in range(3):
            for j in range(3):
                time.sleep(2)
                baseM.showText(".",end="",screen)
                player.timeClimbing+=2
            baseM.showText(,screen)
        waitp2(player, screen)
    elif ch1.title() in ["Leave","L"]:
        baseM.showText("You exit the room without a sound.",screen)
    else:
        baseM.checkCommands(ch1, player)
        wait(player, True)
    return player

def run(player, screen):
    baseM.showText("At the center of the room lies a large golden tree. The branches look sharp and irregular..",screen)
    baseM.showText("You approach the tree. Your urge to steal the golden leaves is almost irresistible...",screen)
    choice = baseM.showText("[Steal Leaves, Break Branches, Destroy Tree, Wait, Leave]",screen)
    if choice.title() in ["Steal", "Rob", "Leaves", "Leaf", "S", "Steal Leaves"]:
        stealLeaves(player, screen)
    elif choice.title() in ["Break", "Branches", "Branch", "Brk", "B", "Break Branches"]:
        baseM.showText("You break off a branch of the tree. It's a lot heavier than you expected, and its irregular, sharp edges cut you.",screen)
        pScript.earnGold(player, 163)
        pScript.damage(player, 30)
    elif choice.title() in ["Destroy", "Tree", "D", "Destroy Tree"]:
        destree(player, screen)
    elif choice.title() in ["Wait", "Stay", "Stand", "W"]:
        wait(player, screen)
    elif choice.title() in ["Leave", "L"]:
        baseM.showText("You leave the room, not wanting to be greedy. [Continue]",screen)
    else:
        baseM.checkCommands(choice, player)
        run(player, screen)
    return player





