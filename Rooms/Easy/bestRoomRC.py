import itemStats
import baseM
#Needs to be updated to have a loop in the first prompt for user input
def run(player):
    print("""The hallway opens up into a fork.
Down one path you see a fountain bubbling with clear, pure, water, and down
the other you see a golden door. 
Choose your path [Fountain, Gold]""")
    choice=input().title()
    if choice in ["Fountain","F"]:
        print("Do you wish to drink from the fountain? [yes, no]")
        choice=input()
        if choice in ["yes", "y","okay","ok"]:
            print("You feel the water purify and heal your body")
            print("You were healed to full health!")
            player.health = player.maxHp
            return player
        elif choice in ["no", "n"]:
            print("You continue on your way, wondering what could have been")
            return player
        else:
            print("Sorry, that is not one of your choices")
    elif choice in ["Gold", "G"]:
        print("""You reach the golden door. What would you like to do?
Press 1 to knock on the door
Press 2 to try to break open the door
Press 3 to cut off pieces of gold and steal them
Press 4 to search the room for a key
Press 5 to leave""")
        while True:
            choice=input().title()
            if choice in ["1", "one", "knock"]:
                print ("""The door opens into a room full of treasure. Gold coins are scattered throughout the chamber, but two incongruencies catch your eye.
A pair of large dice lie near the right wall of the room, while a staff made of pure gold leans against the left wall.
What would you like to do?
Press 1 to gather gold coins, then leave
Press 2 to investigate the dice
Press 3 to take the staff""")
                while True:
                    choice=input()
                    if choice in ["1", "one", "gather"]:
                        print ("Good thing you didn't try to desecrate the door. Cheaters never prosper")
                        print ("You gained 200 gold!")
                        player.gold+=200
                        return player
                    elif choice in ["2", "two", "investigate"]:
                        print ("You roll the dice and get a 6!")
                        print ("Staff of Luck was added to your inventory")
                        player.items.append(itemStats.staffOfLuck)
                        return player
                    elif choice in ["3", "three", "take"]:
                        print ("You pick up the staff")
                        print ("Staff of Gold was added to your inventory!")
                        player.items.append(itemStats.staffOfGold)
                        return player
                    else:
                        print("Sorry, That is not one of your choices")
            elif choice in ["2", "two", "break"]:
                print ("You chip off some gold but ultimately accomplish nothing. You leave, disappointed.")
                player.gold+=25
                return player
            elif choice in ["3", "three", "steal"]:
                print ("You gain 50 gold but ruin the door in the process")
                player.gold+=50
                return player
            elif choice in ["4", "four", "search"]:
                print ("Though you don't find a key, you do find a dusty magic wand leaning in the corner.")
                print ("Wand of Confusion was added to your inventory!")
                player.items.append(itemStats.wandOfConfusion)
                return player
            elif choice in ["5", "five", "leave"]:
                print ("You leave the room.")
                return player
            else:
                print ("Sorry, that is not one of your choices")
    else:
        print("Sorry, that is not one of your choices")
        
