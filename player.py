import pygame
from globals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, disp_surf) -> None:
        super().__init__()
        self.surf = pygame.draw.rect(disp_surf, 'red', (0, WINDOW_HEIGHT / 2, 25, 200))
        self.direction = pygame.Vector2()
        self.speed = 5
        
    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        
    def move(self):
        self.surf += self.direction.y * self.speed
        
    def update(self):
        self.input()
        self.move()