import sys

sys.path.insert(0, 'dependencies')
import baseM, itemStats

def ignore(player):
    print("You walk past the heart to the door at the end of the room.")
    choice = input("The door slams shut! Next to it lies a slip of paper in a crack in the wall..[Take Paper, Leave it]")
    if choice.title() in ["Take", "T", "Paper", "P", "Take Paper"]:
        print("As you grab the paper, the heart begins draining your life. ")
        print("You take the paper, and the door opens slowly")
        print("As soon as the door opens you hurry through and escape to the next room while the heart remains trapped in its own.")
        input("You take 20 damage.")
        player.health -= 20
        baseM.checkPlayer(player)
    elif choice.title() in ["Leave", "L", "Leave It"]:
        print("The heart moves toward you and you feel the life start to slowly drain from your body.")
        for i in player.items:
            try:
                if issubclass(i, itemStats.basicSword):
                    print("You attack the door with your weapons, ultimately destroying it.")
                    player.health -= 30
                    input("You take 30 damage.")
                    baseM.checkPlayer(player)
                    return
            except TypeError:
                pass
        print("You cannot open the door, and the heart fully drains your life.")
        player.health = 0
        player.alive = False
    else:
        baseM.checkCommands(choice, player)
        ignore(player)

def run(player):
    # runs the room
    print("You enter a room and see a bluish-purple heart floating in the middle...")
    choice = input("What do you do? [Attack, Ignore, Run]\n")
    if choice.title() in ["Attack", "A", "Atk"]:
        print("You prepare to attack the heart. It bleeds but is ultimately unharmed.")
        print("The heart suddenly attacks you back! You try to defend but your best efforts seem in vain...")
        dmg = player.health -1
        player.health = 1
        player.items.append(baseM.corruptBlood())
        sel = input("You take {} damage... As you escape you find a bottle of bluish-purple liquid in your bag... [Continue]".format(dmg))
    elif choice.title() in ["Ignore", "I"]:
        ignore(player)
    elif choice.title() in ["Run", "R"]:
        print("You flee the room as fast as your legs can take you. Looking back, you see the heart slowly moving toward you...")
        print("As you succumb to exhaustion, the heart hovers above you. Your consciousness fades as the heart drains the life from your veins...")
        print("You take {} damage.".format(player.health))
        player.health = 0
        player.alive = False
    else:
        baseM.checkCommands(choice, player)
        run(player)
    return player
