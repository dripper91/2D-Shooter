import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y