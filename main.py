#!/usr/bin/env python3
"""
Make It Rain - Main Entry Point

A Payday-like heist game built with Python and Pygame.
"""

import pygame
import sys
from game_manager import GameManager


def main():
    """Initialize and run the game"""
    pygame.init()
    
    print("Make It Rain - Starting...")
    game = GameManager()
    game.run()
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
