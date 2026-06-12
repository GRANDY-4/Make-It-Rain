"""
Game Manager - Core game logic and state management
"""

import pygame
from enum import Enum
from player import Player


class GameState(Enum):
    """Game state enumeration"""
    MENU = "menu"
    LOADING = "loading"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"


class GameManager:
    """Main game manager - handles game loop and state"""
    
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Make It Rain - Heist Game")
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = GameState.PLAYING
        self.fps = 60
        
        # Game objects
        self.player = Player(self.width / 2, self.height / 2)
        
        # Font for debug text
        self.font = pygame.font.Font(None, 24)
    
    def handle_input(self):
        """Handle player input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_p:
                    # Toggle pause
                    if self.state == GameState.PLAYING:
                        self.state = GameState.PAUSED
                    elif self.state == GameState.PAUSED:
                        self.state = GameState.PLAYING
        
        # Continuous key input for movement
        keys = pygame.key.get_pressed()
        self.player.handle_input(keys)
    
    def update(self, delta_time):
        """Update game logic"""
        if self.state == GameState.PLAYING:
            self.player.update(delta_time, self.width, self.height)
    
    def draw(self):
        """Render everything"""
        # Clear screen
        self.screen.fill((0, 0, 0))
        
        # Draw game objects
        self.player.draw(self.screen)
        
        # Draw debug info
        self._draw_debug_info()
        
        # Update display
        pygame.display.flip()
    
    def _draw_debug_info(self):
        """Draw debug information on screen"""
        debug_texts = [
            f"Make It Rain - Heist Game",
            f"FPS: {self.clock.get_fps():.1f}",
            f"Player Pos: ({self.player.x:.1f}, {self.player.y:.1f})",
            f"State: {self.state.value.upper()}",
            f"Controls: WASD=Move | P=Pause | ESC=Exit"
        ]
        
        for i, text in enumerate(debug_texts):
            surface = self.font.render(text, True, (0, 255, 0))
            self.screen.blit(surface, (10, 10 + i * 25))
    
    def run(self):
        """Main game loop"""
        while self.running:
            delta_time = self.clock.tick(self.fps) / 1000.0  # Convert to seconds
            
            self.handle_input()
            self.update(delta_time)
            self.draw()
        
        print("Game closed. Thanks for playing!")
