#NOTICE: This is currently a WIP and is not ready to be used.

import pygame, sys, random, math
from PIL import Image, ImageDraw, ImageFont

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

def dispText(text, screen):
    try:
        pygame.init()
        box = pygame.image.load('resources/textBox.png')
        box_size = box.get_size()
        screen.blit(box, (0, 420)) # modify to make it scalable with screen size
        if len(text) <= 92:
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
                    if [i in text for i in ['[',',',']']] == [True, True, True]:
                        if event.key in range(49, 57):
                            l = text.split('[')[1].split(']')[0].split(', ') #assumes there's only one '[' in the string..
                            try:
                                return l[event.key-49]
                            except IndexError:
                                baseM.showText("Index out of bounds")
                    else:
                        return None
    except ValueError:#pygame.error: 
        baseM.showText("error with displaying text.")


