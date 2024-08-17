import pygame
from globals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups) -> None:
        super().__init__(groups)
        self.surf = pygame.Surface((60, 100))
        self.image = self.surf
        self.image.fill('red')
        self.rect = self.image.get_frect(center = (0, WINDOW_HEIGHT / 2))
        self.position = pygame.Vector2()
        self.speed = 2
        
    def input(self):     
        keys = pygame.key.get_pressed()  
        if keys[pygame.K_DOWN] and self.rect.bottom <= WINDOW_HEIGHT:
            self.position.y = 1
        elif keys[pygame.K_UP] and self.rect.top >= 0:
            self.position.y = -1
        else:
            self.position.y = 0
    
    def move(self):
        self.rect.y += self.position.y * self.speed
        
    def update(self):
        self.input()
        self.move()