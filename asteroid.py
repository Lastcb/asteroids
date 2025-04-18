import pygame, random
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

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            A1 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
            A2 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
            A1.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle) * 1.2
            A2.velocity = pygame.math.Vector2.rotate(self.velocity, -random_angle) *1.2
