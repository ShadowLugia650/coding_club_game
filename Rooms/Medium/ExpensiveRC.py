def run(player):
    print("The hallway opens into a wide chamber lined with gold. You estimate that it will take three minutes to cross the long chamber")
    print("Do you wish to pick up any of the gold lining the hallway?")
    choice=input("[Yes, No]")
    if choice.lower() in ["yes", "y"]:
        print("How much?")
        while True:
            try:
                choice=int(input())
                if choice<0:
                    print("choose a positive number")
                elif choice>10000:
                    print("choose a smaller number")
                else:
                    player.gold+=choice
                    break
            except ValueError:
                print("That's not a number")
    for j in range(3):
        dropGold(player)
        owMoney(player)
    print("You exit the room, and the remaining gold in your sack cools to a comfortable temperature")
    return player
    
    
    
def owMoney(player):
    player.health -= round(player.gold/100)
    print("The money in your sack grows ever hotter. You lose "+str(round(player.gold/100))+" health")
def dropGold(player):
    print("""The gold in your sack seems to be getting warmer as you proceed through the hall. Uncomfortably warm, in fact.
Would you like to drop any?""")
    choice=input("[Yes, No]")
    if choice.lower() in ["yes","y"]:
        print("How much?")
        while True:
            try:
                choice=int(input())
                if choice<0:
                    print("choose a positive number")
                elif choice>player.gold:
                    print("you don't have enough gold")
                else:
                    player.gold-=choice
                    break
            except ValueError:
                print("That's not a number")
