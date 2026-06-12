"""
Player Controller - Handles player movement and state
"""

import pygame


class Player:
    """Player character"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32
        self.speed = 200  # pixels per second
        self.velocity_x = 0
        self.velocity_y = 0
        self.color = (0, 255, 0)  # Green
    
    def handle_input(self, keys):
        """Handle keyboard input"""
        self.velocity_x = 0
        self.velocity_y = 0
        
        if keys[pygame.K_w]:
            self.velocity_y = -self.speed
        if keys[pygame.K_s]:
            self.velocity_y = self.speed
        if keys[pygame.K_a]:
            self.velocity_x = -self.speed
        if keys[pygame.K_d]:
            self.velocity_x = self.speed
    
    def update(self, delta_time, screen_width, screen_height):
        """Update player position"""
        # Update position based on velocity
        self.x += self.velocity_x * delta_time
        self.y += self.velocity_y * delta_time
        
        # Clamp to screen bounds
        self.x = max(0, min(self.x, screen_width - self.width))
        self.y = max(0, min(self.y, screen_height - self.height))
    
    def draw(self, surface):
        """Draw the player on screen"""
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(surface, self.color, rect)
    
    def get_rect(self):
        """Get player collision rect"""
        return pygame.Rect(self.x, self.y, self.width, self.height)
