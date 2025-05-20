class Hero:
    def __init__(self, name, x, y, color, size=(1, 1), health=100, shields=0, movement=6, 
                 jump=2, jump_type="jump", clamber=0, attack_range=1):
        self.name = name
        self.x = x  # Grid x-position
        self.y = y  # Grid y-position
        self.z = 0  # Elevation (z-axis)
        self.color = color
        self.size = size  # (width, height) in tiles
        self.health = health
        self.shields = shields
        self.movement = movement
        self.jump = jump
        self.jump_type = jump_type  # "jump", "glide", "hover", "fly"
        self.clamber = clamber
        self.attack_range = attack_range
        self.cards = []  # Placeholder for 32-card deck

    def draw(self, screen, tile_size):
        pygame.draw.rect(screen, self.color, 
                        (self.x * tile_size, self.y * tile_size, 
                         self.size[0] * tile_size, self.size[1] * tile_size))

# Example usage in the game loop
heroes = [
    Hero("Warrior", 5, 5, (255, 0, 0), size=(1, 1), health=120, movement=6, jump=2, jump_type="jump"),
    Hero("Glider", 10, 10, (0, 255, 0), size=(2, 2), movement=8, jump=3, jump_type="glide")
]

# Updated game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (SCREEN_WIDTH, y))

    # Draw all heroes
    for hero in heroes:
        hero.draw(screen, TILE_SIZE)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
