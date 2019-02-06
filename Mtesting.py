def specials(Input, player):
    if "addItem " in Input:
        itm = Input.split("addItem ")[1]
        player.items.append(itm)
    elif "setHealth " in Input:
        health = Input.split("setHealth ")[1]
        player.health = int(health)
    elif "setGold " in Input:
        gold = Input.split("setGold ")[1]
        player.gold = int(gold)
