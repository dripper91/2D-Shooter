import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, groups):
        super().__init__(groups)
        self.image = pygame.Surface([50, 50])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(topleft = (x,y))
        self.speed = 10
        self.direction = pygame.math.Vector2()
        self.x = x
        self.y = y

    def update(self):
        self.x_change = 0
        self.y_change = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and not keys[pygame.K_d]:
            self.x_change -= self.speed
            self.direction.x = -1
        elif keys[pygame.K_d] and not keys[pygame.K_a]:
            self.x_change += self.speed
            self.direction.x = 1
        else:
            self.direction.x = 0
        if keys[pygame.K_w] and not keys[pygame.K_s]:
            self.y_change -= self.speed
            self.direction.y = -1
        elif keys[pygame.K_s] and not keys[pygame.K_w]:
            self.y_change += self.speed
            self.direction.y = 1
        else:
            self.direction.y = 0

