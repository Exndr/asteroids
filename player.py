import pygame
from constants import *
from circleshape import CircleShape #import the module

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)  # Call the parent class constructor
        self.rotation = 0  # Initialize rotation to 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        
        # Calculate the triangle's vertices
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt  # Update rotation based on dt

    
    def update(self, dt):
        keys = pygame.key.get_pressed()


        if keys[pygame.K_a]:  # If the "A" key is pressed
            self.rotate(-dt)  # Rotate left (invert dt)
        if keys[pygame.K_d]:  # If the "D" key is pressed
            self.rotate(dt)  # Rotate right