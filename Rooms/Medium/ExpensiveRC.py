def run(player):
    print("The hallway opens into a wide chamber lined with gold. You estimate that it will")
    
    
def owMoney(player):
    player.health -= round(player.gold/100)
    print("The money in your sack grows ever hotter. You lose "+str(round(player.gold/100))+" health")
