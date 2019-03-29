#NOTICE: This is currently a WIP and is not ready to be used.

import pygame, sys, random, math, spriteClasses
from spriteClasses import *
from pScript import PChar
#from PIL import Image, ImageDraw, ImageFont

def initScreen():
    size = (720, 540)
    pygame.init()
    screen = pygame.display.set_mode(size)
    return screen

def initSprites(get : list = []):
    #Initializes the sprites of every item in the list.
    #Returns a list of initialized sprites.
    #Automatically initializes basic sprites such as bag, curses, etc.
    from baseM import basicEnemy
    sprites = pygame.sprite.Group(Bag())
    for i in get:
        if type(i) == PChar:
            sp = Player()
        elif issubclass(type(i), basicEnemy):
            sp = eval(i.type.title().replace(" ",""))()
        elif issubclass(type(i), basicItem):
            sp = eval(i.name.title().replace(" ",""))()
        sprites.add(sp)
    return sprites
    
def runBattle(player, enemies, screen):
    pygame.init()
    bg = pygame.image.load('resources/background.png')
    initSprites([player] + enemies)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if baseM.getFirstAliveEnemy(enemies) is None: dispText(player, "You defeated all the enemies! [Continue]", screen)
        screen.blit(bg, (0,0))
        screen.blit(player, (70, 70))
        pygame.display.flip()

def keyPresses(player, event):
    pass

def clickables(player, pos, sprites):
    clicked = [s for s in sprites if s.rect.collidepoint(pos)]
    for sprite in clicked:
        if type(sprite) == Bag:
            
            pass # Show bag on screen

def dispText(player, text, screen):
    try:
        pygame.init()
        if player is not None:
            refreshScreen(player, screen)
            sprites = initSprites([player])
        box = pygame.image.load('resources/textBox.png')
        box_size = box.get_size()
        screen.blit(box, (0, 420)) # modify to make it scalable with screen size
        if '\n' in text:
            txt = text.split('\n')
            check = True
            for i in txt:
                if len(i) > 87:
                    check = False
                    break
            if check:
                txs = [pygame.font.Font(None, 22).render(i, True, (255,255,255)) for i in txt]
                for i in range(len(txs)):
                    screen.blit(txs[i], (box_size[0]/2-txs[i].get_size()[0]/2, 440+20*i))
        if '\n' not in text or not check:
            if '\n' in text:
                text = text.replace('\n','')
            if len(text) <= 87:
                tx = pygame.font.Font(None, 22).render(text, True, (255,255,255))
                screen.blit(tx, (box_size[0]/2-tx.get_size()[0]/2, 440))
            else:
                txt = text.split(' ')
                txts = []
                for i in range(math.ceil(len(text)/87)):
                    txts.append('')
                for i in txt:
                    for j in range(len(txts)):
                        if (len(txts[j]) + len(i)) <= 87:
                            txts[j] += i + ' '
                            break
                print(txts)
                print(txt)
                txs = [pygame.font.Font(None, 22).render(i, True, (255,255,255)) for i in txts]
                for i in range(len(txs)):
                    screen.blit(txs[i], (box_size[0]/2-txs[i].get_size()[0]/2, 440+20*i))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    keyPresses(player, event)
                    if [i in text for i in ['[',',',']']] == [True, True, True] and ',' in text.split('[')[1].split(']')[0]:
                        if event.key in range(49, 57):
                            l = text.split('[')[1].split(']')[0].split(', ') #assumes there's only one '[' in the string..
                            try:
                                return l[event.key-49]
                            except IndexError:
                                print("Index out of bounds")
                    else:
                        return None
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    clickables(player, pos, sprites)
    except pygame.error: 
        print("error with displaying text.")

def refreshScreen(player, screen):
    #assumes screen is not None.
    pygame.init()
    box = pygame.image.load('resources/healthBox.png')
    sprites = initSprites()
    sprites.draw(screen)
    screen.blit(box, (0,0))
    screen.blit(pygame.font.Font(None, 31).render("HP", True, (255,0,0)), (9,23))
    pygame.draw.rect(screen, (255,0,0), (63,27,(player.health/player.maxHp)*258,12))
    screen.blit(pygame.font.Font(None, 17).render("{}/{}".format(player.health, player.maxHp), True, (255,0,0)), (159,41))
    screen.blit(pygame.font.Font(None, 31).render("{}".format(player.gold), True, (255,144,0)), (65, 72))
    pygame.display.flip()
