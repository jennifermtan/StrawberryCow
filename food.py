import pygame
import random
import os
import config

class Food(pygame.sprite.Sprite):
    def __init__(self, x, y, image): 
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, config.WIDTH - self.rect.width)
        self.rect.y = 0 - self.rect.width
        self.speed = random.randrange(5, 10)
    
    def update(self):
        self.rect.move_ip(0, self.speed)
        display_rect = pygame.display.get_surface().get_rect()
        if self.rect.top > display_rect.bottom:
            return True
        return False