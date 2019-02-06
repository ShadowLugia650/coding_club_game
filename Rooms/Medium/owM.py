import sys

sys.path.insert(0, 'dependencies')
import baseM

def run(player):
    # runs the room
    print("You enter a room and see a bluish-purple heart floating in the middle...")
    choice = input("What do you do? [Attack, Run]\n")
    if choice.title() in ["Attack", "A", "Atk"]:
        print("You prepare to attack the heart. It bleeds but is ultimately unharmed.")
        print("The heart suddenly attacks you back! You try to defend but your best efforts seem in vain...")
        dmg = player.health -1
        player.health = 1
        player.items.append("Corrupt Blood") #heal x amount each time you go up a floor
        sel = input("You take {} damage... As you escape you find a bottle of bluish-purple liquid in your bag... [Continue]".format(dmg))
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

