import pygame
from src.prey import Prey
from src.obst import Obsticle
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
        
    def draw_preys(self,prey) -> None:
            pygame.draw.rect(self.screen, "white", prey.rect)

    # def init_obsticles(self,obsticles:Obsticle) -> None:
    #     self.obsticles = obsticles
    #     print("Obsticle initialized")

    def start_screen(self) -> None:
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill("green")

            # try:
            #     self.obsticles.draw_obsticle(self.screen)
            #     print(self.dt)
            #     if self.obsticles.collision(self.preys[0].rect):
            #         self.preys[0].is_alive = False
            #         print("Collision detected")
            #         del self.obsticles
            # except Exception as e:
            #     print("Obsticle not initialized: {}".format(e))
            
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
                            

                    if prey.is_alive == False and prey.is_collide:
                        self.preys.remove(prey)
                        print("Prey is dead")
                        self.preys.append(Prey(random.randint(0, 800), random.randint(0, 800)))
                        print("New Prey is born")
                    elif prey.is_alive == False and not prey.is_collide:
                        self.preys.remove(prey)
                        print("Prey is dead alone")
                    else:
                        pass
                        
            except Exception as e:
                print("Player not initialized: {}".format(e))


            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000
        pygame.quit()

        