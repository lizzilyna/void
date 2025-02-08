import sys
import pygame
from settings import Settings

class Void:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.bg_color = (self.settings.bg_color)
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
      


    def run_game(self):
        while True:    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(event.key) #scopo del "gioco": stampa in console il codice numerico dei tasti premuti
                
            self.screen.fill(self.bg_color)
            pygame.display.flip()
            self.clock.tick(60)

     
                

                

if __name__=='__main__':
    vi = Void()
    vi.run_game()
