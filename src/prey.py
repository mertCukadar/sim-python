import pygame
import time
import random

class Prey:
    def __init__(self , x: int , y:int):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.is_alive = True
        self.birth_time = time.time()
        self.life_time = 20
        self.direction = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        self.random_direction = random.choice(self.direction)
        self.is_collide = False


    def out_of_time(self):
        self.current_time = time.time()
        if self.current_time - self.birth_time > self.life_time:
            self.is_alive = False
            print("Prey is dead")
            

    def move(self, dt: float) -> None:
        self.rect.x += self.random_direction[0] * 400 * dt
        self.rect.y += self.random_direction[1] * 400 * dt
        if self.rect.x < 50 or self.rect.x > 700 or self.rect.y < 50 or self.rect.y > 700:
            self.random_direction = random.choice(self.direction)


    def collision_neihbor(self, prey) -> bool:
        return self.rect.colliderect(prey.rect)
   
    def is_collison_setter(self):
        self.is_collide = True