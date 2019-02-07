def specials(Input, player):
    if "addItem " in Input:
        itm = Input.split("addItem ")[1]
        try:
            player.items.append(eval(itm)())
        except NameError:
            pass
    elif "setHealth " in Input:
        health = Input.split("setHealth ")[1]
        player.health = int(health)
    elif "setGold " in Input:
        gold = Input.split("setGold ")[1]
        player.gold = int(gold)
