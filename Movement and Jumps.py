class GameMap:
    def __init__(self, width=32, height=24):
        # 3D grid: [x][y][z] where z is elevation (0 is ground, higher is elevation)
        self.grid = [[[0 for _ in range(10)] for _ in range(height)] for _ in range(width)]
        # Example obstacle: height 2 at (6, 5)
        self.grid[6][5][1] = 2  

    def can_move(self, hero, new_x, new_y, new_z):
        # Check bounds
        if not (0 <= new_x < GRID_WIDTH and 0 <= new_y < GRID_HEIGHT):
            return False
        
        # Check size and obstacles
        for dx in range(hero.size[0]):
            for dy in range(hero.size[1]):
                x, y = new_x + dx, new_y + dy
                if x >= GRID_WIDTH or y >= GRID_HEIGHT or self.grid[x][y][new_z] > 0:
                    return False
        return True

    def calculate_jump(self, hero, dx, dy):
        distance = abs(dx) + abs(dy)  # Manhattan distance for simplicity
        if distance > hero.movement:
            return None  # Too far
        
        mid = distance / 2
        max_height = hero.jump
        if hero.jump_type == "jump":
            # Check midpoint obstacle
            mid_x = hero.x + int(dx * mid / distance) if distance else hero.x
            mid_y = hero.y + int(dy * mid / distance) if distance else hero.y
            if self.grid[mid_x][mid_y][1] > max_height:
                return None
            new_x, new_y = hero.x + dx, hero.y + dy
            if self.can_move(hero, new_x, new_y, 0):
                return (new_x, new_y, 0)
        # Add glide, hover, fly logic here later
        return None

# Integrate into game
game_map = GameMap()

# Example: Move hero with keyboard (basic test)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            dx, dy = 0, 0
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_UP:
                dy = -1
            elif event.key == pygame.K_DOWN:
                dy = 1
            if dx or dy:
                new_pos = game_map.calculate_jump(heroes[0], dx, dy)
                if new_pos:
                    heroes[0].x, heroes[0].y, heroes[0].z = new_pos

    # Drawing code remains the same
    screen.fill(WHITE)
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (SCREEN_WIDTH, y))
    for hero in heroes:
        hero.draw(screen, TILE_SIZE)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
