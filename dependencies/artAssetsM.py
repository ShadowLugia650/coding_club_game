#NOTICE: This is currently a WIP and is not ready to be used.

import pygame, sys, random
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
            #if baseM.getFirstAliveEnemy(enemies) is None: figure this out
        screen.blit(bg, (0,0))
        screen.blit(player, (70, 70))
        pygame.display.flip()

def dispText(text, screen):
    try:
        pygame.init()
        box = pygame.image.load('resources/textBox.png')
        box_size = box.get_size()
        screen.blit(box, (0, 420)) # modify to make it scalable with screen size
        tx = pygame.font.Font(None, 22).render(text, True, (255,255,255))
        screen.blit(tx, (box_size[0]/2-tx.get_size()[0]/2, 440))
        pygame.display.flip()
    except ValueError:#pygame.error: 
        print("error with displaying text.")
