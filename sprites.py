import pygame
from globals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups) -> None:
        super().__init__(groups)
        #image
        self.surf = pygame.Surface((60, 100))
        self.image = self.surf
        self.image.fill('red')
        #movement
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
      

class Player2(pygame.sprite.Sprite):
    def __init__(self, groups) -> None:
        super().__init__(groups)
        #image
        self.surf = pygame.Surface((60, 100))
        self.image = self.surf
        self.image.fill('green')
        #movement
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH, WINDOW_HEIGHT / 2))
        self.position = pygame.Vector2()
        self.speed = 2
        
    def input(self):     
        keys = pygame.key.get_pressed()  
        if keys[pygame.K_s] and self.rect.bottom <= WINDOW_HEIGHT:
            self.position.y = 1
        elif keys[pygame.K_w] and self.rect.top >= 0:
            self.position.y = -1
        else:
            self.position.y = 0
    
    def move(self):
        self.rect.y += self.position.y * self.speed
        
    def update(self):
        self.input()
        self.move()  

class Ball(pygame.sprite.Sprite):
    def __init__(self, player1, player2, groups) -> None:
        super().__init__(groups)
        #image
        self.image = self.surf = pygame.Surface((BALL_WIDTH, BALL_HEIGHT))
        pygame.draw.circle(self.image, 'blue', (BALL_WIDTH/ 2, BALL_HEIGHT/ 2), 20)
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        #movement
        self.position = pygame.Vector2(1, 1)
        self.speed = 0.5
        self.player1 = player1
        self.player2 = player2
        
    def move(self):
        # Standard movement
        self.rect.center += self.position * self.speed
        
        # Bouncing
        if self.rect.bottom >= WINDOW_HEIGHT:
            self.position.y = -1
        elif self.rect.top == 0:
            self.position.y = 1
        elif pygame.FRect.colliderect(self.player1.rect, self.rect):
            self.position.x = 1
        elif pygame.FRect.colliderect(self.player2.rect, self.rect):
            self.position.x = -1
        elif self.rect.right == 0 or self.rect.left >= WINDOW_WIDTH:
            self.kill()
            
        print(f'{self.rect}')
        
    def update(self):
        self.move()
        

