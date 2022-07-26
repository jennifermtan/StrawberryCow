import pygame
import os
import config

class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Sprite, self).__init__()
        self.x = x
        self.y = y
        self.movex = 0 #move along x axis
        self.image = pygame.image.load(os.path.join("images", "strawberry_cow.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.score = 0

    def update(self):
        #Update the sprite position
        self.rect.x += self.movex

        #Check if sprite is off screen, then go to the other side
        if self.rect.x > config.WIDTH:
            self.rect.x = 0 
        if self.rect.x < 0:
            self.rect.x = config.WIDTH       

    def control(self, x):
        #Control the player movement
        self.movex = 0
        self.movex += x
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)