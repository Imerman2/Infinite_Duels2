Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
GRID_WIDTH, GRID_HEIGHT = 32, 24
TILE_SIZE = 20  # Pixels per tile
SCREEN_WIDTH = GRID_WIDTH * TILE_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * TILE_SIZE
FPS = 60

... # Colors
... WHITE = (255, 255, 255)
... BLACK = (0, 0, 0)
... RED = (255, 0, 0)
... BLUE = (0, 0, 255)
... 
... # Set up the display
... screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
... pygame.display.set_caption("Board Game Prototype")
... clock = pygame.time.Clock()
... 
... # Game loop
... running = True
... while running:
...     for event in pygame.event.get():
...         if event.type == pygame.QUIT:
...             running = False
... 
...     # Clear screen
...     screen.fill(WHITE)
... 
...     # Draw grid
...     for x in range(GRID_WIDTH):
...         for y in range(GRID_HEIGHT):
...             pygame.draw.rect(screen, BLACK, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
... 
...     # Example: Draw two heroes (colored squares)
...     pygame.draw.rect(screen, RED, (5 * TILE_SIZE, 5 * TILE_SIZE, TILE_SIZE, TILE_SIZE))  # 1x1 hero
...     pygame.draw.rect(screen, BLUE, (10 * TILE_SIZE, 10 * TILE_SIZE, TILE_SIZE * 2, TILE_SIZE * 2))  # 2x2 hero
... 
...     # Update display
...     pygame.display.flip()
...     clock.tick(FPS)
... 
... pygame.quit()
