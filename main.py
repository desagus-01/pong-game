import pygame
from globals import *
from sprites import Player, Ball

class Game:
    
    def __init__(self) -> None:
        # set-up
        pygame.init()
        self.display_surf = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('')
        self.running = True
        self.group = pygame.sprite.Group()
        self.player = Player(self.group)
        self.ball = Ball(self.group)
        
    def game_loop(self):
        while self.running:
            
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            # Updates
            self.group.update()
            
            # draw game
            self.display_surf.fill('black')
            self.group.draw(self.display_surf) 
            
            # Update images
            pygame.display.update()
            
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.game_loop()