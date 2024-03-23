import pygame
from src.prey import Prey

class Map:
    def __init__(self , x_width:int, y_height:int):
        pygame.init()
        self.screen = pygame.display.set_mode((x_width, y_height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0

    def init_player(self,preys:list[Prey]) -> None:
        self.preys = preys
        
    def draw_preys(self,prey) -> None:
            pygame.draw.circle(self.screen, "red", prey.player_pos, 40)

    def start_screen(self) -> None:
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill("green")
            
            try:
                for prey in self.preys:
                    self.draw_preys(prey)
                    prey.move(self.dt)
            except Exception as e:
                print("Player not initialized: {}".format(e))

            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000
        pygame.quit()

        