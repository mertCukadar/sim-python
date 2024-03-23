import pygame

class Obsticle:
    def __init__(self , x:int , y:int):
        self.rect = pygame.Rect(x, y, 100, 100)
    
    def draw_obsticle(self, screen) -> None:
        pygame.draw.rect(screen, "black", self.rect)

    # collision
    def collision(self, prey) -> bool:
        return self.rect.colliderect(prey)
    
    def dead(self):
        del self.rect