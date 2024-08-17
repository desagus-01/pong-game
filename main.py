import pygame
from globals import *
from player import Player

class Game:
    
    def __init__(self) -> None:
        # set-up
        pygame.init()
        self.display_surf = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.running = True
        self.player = Player(self.display_surf)
        
    def game_loop(self):
        while self.running:
            
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            # draw game
            self.display_surf.fill('black')
            self.player.update()
            
            # Update images
            pygame.display.update()
            
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.game_loop()