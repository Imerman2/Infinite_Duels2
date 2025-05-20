import pygame

# Initialize Pygame
pygame.init()

# Screen settings
GRID_WIDTH, GRID_HEIGHT = 32, 24
TILE_SIZE = 20  # Pixels per tile
SCREEN_WIDTH = GRID_WIDTH * TILE_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * TILE_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Card Game Battlemap")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)  # Example hero color

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(WHITE)

    # Draw grid
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (SCREEN_WIDTH, y))

    # Draw a hero (example: 1x1 red square at grid position (5, 5))
    hero_x, hero_y = 5, 5
    pygame.draw.rect(screen, RED, (hero_x * TILE_SIZE, hero_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Update display
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
