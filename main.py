import pygame
import sys
from game_manager import GameManager

def main():
    """Main entry point for the game"""
    pygame.init()
    
    # Create game manager and run
    game = GameManager()
    game.run()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
