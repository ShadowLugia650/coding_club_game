#NOTICE: This is currently a WIP and is not ready to be used.

import pygame, sys, random, math
#from PIL import Image, ImageDraw, ImageFont

def initScreen():
    size = (720, 540)
    pygame.init()
    screen = pygame.display.set_mode(size)
    return screen
    
def runBattle(player, enemies, screen):
    pygame.init()
    bg = pygame.image.load('resources/background.png')
    player = None
    try:
        player = pygame.image.load("resources/player.png")
    except pygame.error:
        player = pygame.image.load("resources/placeholder.png")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if baseM.getFirstAliveEnemy(enemies) is None: dispText("You defeated all the enemies! [Continue]")
        screen.blit(bg, (0,0))
        screen.blit(player, (70, 70))
        pygame.display.flip()

def dispText(player, text, screen):
    try:
        pygame.init()
        if player is not None:
            refreshScreen(player, screen)
        box = pygame.image.load('resources/textBox.png')
        box_size = box.get_size()
        screen.blit(box, (0, 420)) # modify to make it scalable with screen size
        if '\n' in text:
            txt = text.split('\n')
            txs = [pygame.font.Font(None, 22).render(i, True, (255,255,255)) for i in txt]
            for i in range(len(txs)):
                screen.blit(txs[i], (box_size[0]/2-txs[i].get_size()[0]/2, 440+20*i))
        elif len(text) <= 92:
            tx = pygame.font.Font(None, 22).render(text, True, (255,255,255))
            screen.blit(tx, (box_size[0]/2-tx.get_size()[0]/2, 440))
        else:
            txt = text.split(' ')
            txts = []
            for i in range(math.ceil(len(text)/92)):
                txts.append('')
            for i in txt:
                for j in range(len(txts)):
                    if (len(txts[j]) + len(i)) < 92:
                        txts[j] += i + ' '
                        break
            txs = [pygame.font.Font(None, 22).render(i, True, (255,255,255)) for i in txts]
            for i in range(len(txs)):
                screen.blit(txs[i], (box_size[0]/2-txs[i].get_size()[0]/2, 440+20*i))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    import baseM
                    baseM.keyPresses(event, player)
                    if [i in text for i in ['[',',',']']] == [True, True, True] and ',' in text.split('[')[1].split(']')[0]:
                        if event.key in range(49, 57):
                            l = text.split('[')[1].split(']')[0].split(', ') #assumes there's only one '[' in the string..
                            try:
                                return l[event.key-49]
                            except IndexError:
                                print("Index out of bounds")
                    else:
                        return None
    except pygame.error: 
        print("error with displaying text.")

def refreshScreen(player, screen):
    #assumes screen is not None.
    pygame.init()
    box = pygame.image.load('resources/healthBox.png')
    bag = pygame.image.load('resources/bag.png')
    screen.blit(box, (0,0))
    screen.blit(bag, (0,356))
    screen.blit(pygame.font.Font(None, 31).render("HP", True, (255,0,0)), (9,23))
    pygame.draw.rect(screen, (255,0,0), (63,27,(player.health/player.maxHp)*258,12))
    screen.blit(pygame.font.Font(None, 17).render("{}/{}".format(player.health, player.maxHp), True, (255,0,0)), (159,41))
    screen.blit(pygame.font.Font(None, 31).render("{}".format(player.gold), True, (255,144,0)), (65, 72))
    pygame.display.flip()
