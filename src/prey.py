import pygame
import time

class Prey:
    def __init__(self , x: int , y:int):
        self.player_pos = pygame.Vector2(x, y)
        self.is_alive = True
        self.life_time = 100
           

    def move(self, dt: float) -> None:
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_w]:
            self.player_pos.y -= 300 * dt
        if self.keys[pygame.K_s]:
            self.player_pos.y += 300 * dt
        if self.keys[pygame.K_a]:
            self.player_pos.x -= 300 * dt
        if self.keys[pygame.K_d]:
            self.player_pos.x += 300 * dt