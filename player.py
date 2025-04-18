import pygame
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0
    def draw(self, screen):
        return pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            return self.move(dt)
        if keys[pygame.K_a]:
            return self.rotate(-dt)
        if keys[pygame.K_s]:
            return self.move(-dt)
        if keys[pygame.K_d]:
            return self.rotate(dt)
        if keys[pygame.K_SPACE]:
            return self.shoot()
        
        if self.shot_cooldown > 0:
            self.shot_cooldown -= dt


    def shoot(self):
        if self.shot_cooldown <= 0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shot_cooldown = PLAYER_SHOOT_COOLDOWN
        


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
       
