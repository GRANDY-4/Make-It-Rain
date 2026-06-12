"""
Game Entities - Base classes for enemies, NPCs, etc.
"""

import pygame
from abc import ABC, abstractmethod


class Entity(ABC):
    """Base class for all game entities"""
    
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.velocity_x = 0
        self.velocity_y = 0
    
    @abstractmethod
    def update(self, delta_time, screen_width, screen_height):
        """Update entity logic"""
        pass
    
    @abstractmethod
    def draw(self, surface):
        """Draw entity on screen"""
        pass
    
    def get_rect(self):
        """Get entity collision rect"""
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def check_collision(self, other):
        """Check collision with another entity"""
        return self.get_rect().colliderect(other.get_rect())


class Enemy(Entity):
    """Basic enemy entity"""
    
    def __init__(self, x, y, speed=100):
        super().__init__(x, y, 32, 32, (255, 0, 0))  # Red
        self.speed = speed
    
    def update(self, delta_time, screen_width, screen_height):
        """Update enemy logic"""
        # Placeholder: enemies will patrol
        pass
    
    def draw(self, surface):
        """Draw enemy"""
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(surface, self.color, rect)


class Loot(Entity):
    """Loot/objective entity"""
    
    def __init__(self, x, y):
        super().__init__(x, y, 20, 20, (255, 255, 0))  # Yellow
        self.collected = False
    
    def update(self, delta_time, screen_width, screen_height):
        """Update loot logic"""
        pass
    
    def draw(self, surface):
        """Draw loot"""
        if not self.collected:
            rect = pygame.Rect(self.x, self.y, self.width, self.height)
            pygame.draw.rect(surface, self.color, rect)
