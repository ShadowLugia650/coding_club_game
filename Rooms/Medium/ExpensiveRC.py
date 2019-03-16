def run(player, screen):
    baseM.showText("The hallway opens into a wide chamber lined with gold. You estimate that it will take three minutes to cross the long chamber")
    baseM.showText("Do you wish to pick up any of the gold lining the hallway?")
    choice=baseM.showText("[Yes, No]")
    if choice.lower() in ["yes", "y"]:
        baseM.showText("How much?")
        while True:
            try:
                choice=int(baseM.showText())
                if choice<0:
                    baseM.showText("choose a positive number")
                elif choice>10000:
                    baseM.showText("choose a smaller number")
                else:
                    player.gold+=choice
                    break
            except ValueError:
                baseM.showText("That's not a number")
    for j in range(3):
        dropGold(player, screen)
        owMoney(player, screen)
    baseM.showText("You exit the room, and the remaining gold in your sack cools to a comfortable temperature")
    return player
    
    
    
def owMoney(player, screen):
    player.health -= round(player.gold/100)
    baseM.showText("The money in your sack grows ever hotter. You lose "+str(round(player.gold/100))+" health")
def dropGold(player, screen):
    baseM.showText("""The gold in your sack seems to be getting warmer as you proceed through the hall. Uncomfortably warm, in fact.
Would you like to drop any?""")
    choice=baseM.showText("[Yes, No]")
    if choice.lower() in ["yes","y"]:
        baseM.showText("How much?")
        while True:
            try:
                choice=int(baseM.showText())
                if choice<0:
                    baseM.showText("choose a positive number")
                elif choice>player.gold:
                    baseM.showText("you don't have enough gold")
                else:
                    player.gold-=choice
                    break
            except ValueError:
                baseM.showText("That's not a number")



