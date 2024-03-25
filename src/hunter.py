from src.prey import Prey
import pygame
import random

class Hunter(Prey):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.rect = pygame.Rect(x, y, 40, 40)
        self.direction = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        self.random_direction = random.choice(self.direction)
        self.is_collide = False
        
    def collision_to_prey(self, prey):
        return self.rect.collidetect(prey.rect)
    
    