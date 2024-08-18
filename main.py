import pygame
from globals import *
from sprites import Player, Ball

class Game:
    
    def __init__(self, fps) -> None:
        # set-up
        pygame.init()
        self.display_surf = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('')
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 2
        self.fps = fps
        self.group = pygame.sprite.Group()
        self.player = Player(self.group)
        self.ball = Ball(self.group)
    
    def set_dt(self, fps):
        self.dt = self.clock.tick() / fps 
        
    def game_loop(self):
        
        while self.running:
            self.set_dt(self.fps) 
            
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
    game = Game(fps=100)
    game.game_loop()