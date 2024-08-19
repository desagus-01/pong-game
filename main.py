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
        self.player1 = Player((0, WINDOW_HEIGHT / 2), 'red', self.group, True)
        self.player2 = Player((WINDOW_WIDTH, WINDOW_HEIGHT / 2), 'green', self.group, False)
        self.ball = Ball(self.player1, self.player2, self.group)
    
    def set_dt(self, fps):
        self.dt = self.clock.tick() / fps 
        
    def restart(self):
        if not self.ball.on:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.ball = Ball(self.player1, self.player2, self.group)
                self.running = True
        
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

            # New ball to restart
            self.restart()
            
        pygame.quit()


if __name__ == '__main__':
    game = Game(fps=100)
    game.game_loop()