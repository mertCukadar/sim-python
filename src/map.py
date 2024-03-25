import pygame
from src.prey import Prey
from src.hunter import Hunter
import random

class Map:

    def __init__(self , x_width:int, y_height:int):
        pygame.init()
        self.screen = pygame.display.set_mode((x_width, y_height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0

    def init_player(self,preys:list[Prey]) -> None:
        self.preys = preys

    def init_hunter(self,hunter:list[Hunter]) -> None:
        self.hunter = hunter
        
    def draw_preys(self,prey) -> None:
            pygame.draw.rect(self.screen, "white", prey.rect)

    def draw_hunters(self,hunter) -> None:
        pygame.draw.rect(self.screen, "red", hunter.rect)
  
    def start_screen(self) -> None:
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill("green")

            try:
                self.draw_hunters(self.hunter)
                self.hunter.move(self.dt)
                for prey in self.preys:
                    if self.hunter.collision_to_prey(prey):
                        self.preys.remove(prey)
                    
            except Exception as e:
                print("Hunter not initialized: {}".format(e))


            try:
                for prey in self.preys:
                    self.draw_preys(prey)
                    prey.move(self.dt)
                    prey.out_of_time()

                    # Çarpışma algılama ve yeni Prey oluşturma
                    for other_prey in self.preys:
                        if prey != other_prey and prey.collision_neihbor(other_prey):
                            prey.is_collide = True
                            break
                    if not prey.is_alive and prey.is_collide:
                        self.preys.remove(prey)
                        print("Prey is dead")
                        self.preys.append(Prey(random.randint(0, 800), random.randint(0, 800)))
                        self.preys.append(Prey(random.randint(0, 800), random.randint(0, 800)))

                        print("New Prey is born")
                    elif not prey.is_alive and not prey.is_collide:
                        self.preys.remove(prey)
                        print("Prey is dead alone")
                    else:
                        pass
                        
            except Exception as e:
                print("Player not initialized: {}".format(e))


            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000
        pygame.quit()

        