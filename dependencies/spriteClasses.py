import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/player.png')
        self.rect = self.image.get_rect()

class Bag(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/bag.png')
        self.rect = pygame.Rect(0,356, 64, 64)#self.image.get_rect()
