import pygame
from circleshape import CircleShape
from constants import *
    
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        #new_position = pygame.Vector2(self.x, self.y) + (self.velocity * dt)
        #self.x = new_position.x
        #self.y = new_position.y
