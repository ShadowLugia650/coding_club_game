#NOTICE: This is currently WIP and is not ready to be used.

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
        screen.blit()
        tx = pygame.font.Font.render(text)
    except pygame.error: 
        print("error with displaying text.")
