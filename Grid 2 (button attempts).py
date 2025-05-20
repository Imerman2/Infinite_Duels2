import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
GRID_WIDTH, GRID_HEIGHT = 24, 16
TILE_SIZE = 30  # Pixels per tile
SCREEN_WIDTH = GRID_WIDTH * TILE_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * TILE_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Infinite Duels Prototype")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0) 
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
VIOLET = (127, 0, 255)
GRAY = (150, 150, 150) # Example hero color
LIGHT_GRAY = (200, 200, 200)

# DropDown Class for Dropdown Menus for user input
class Dropdown:
    def __init__(self, x, y, width, height, options, label):
        self.rect = pygame.Rect(x, y, width, height)
        self.options = options
        self.label = label
        self.current_option = options[0] # Index of selected options
        self.expanded = False
        self.font = pygame.font.Font(None, 22)
        self.label_surface = self.font.render(label, True, BLACK)

    def draw(self, screen):
        #label
        screen.blit(self.label_surface, (self.rect.x, self.rect.y + 25))
        #main box
        pygame.draw.rect(screen, WHITE, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        #current selection
        text = self.font.render(str(self.current_option), True, BLACK)
        screen.blit(text, (self.rect.x + 5, self.rect.y + 5))
        #The expanded dropdown
        if self.expanded:
            for i, option in enumerate(self.options):
                rect = pygame.Rect(self.rect.x, self.rect.y + (i + 1) * self.rect.height, self.rect.width, self.rect.height)
                pygame.draw.rect(screen, LIGHT_GRAY, rect)
                pygame.draw.rect(screen, RED, rect, 1)
                text = self.font.render(str(option), True, BLACK)
                screen.blit(text, (rect.x + 5, rect.y + 5))

    # What happens on dropdown clicks
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # clicks on dropdowns expand them
            if self.rect.collidepoint(event.pos):
                self.expanded = not self.expanded
            # clicks on things in the expanded dropdown list change the option and close the dropdown
            elif self.expanded:
                for i, option in enumerate(self.options):
                    rect = pygame.Rect(self.rect.x, self.rect.y + (i + 1) * self.rect.height, self.rect.width, self.rect.height)
                    if rect.collidepoint(event.pos):
                        self.current_option = option
                        self.expanded = False
 
# Dropdown Selection Lists  herodropdown is to be deleted for multiselect tool
team_options = [2, 3, 4]
players_options = [1, 2, 3, 4] 
heroes_options = ["White", "Black", "Red", "Orange", "Yellow", "Green", "Blue", "Violet", "Gray", "Light Gray"] 
spawn_options = ["(2,4)", "(2,10)", "(13,4)", "(13,10)"] 

# The Dropdowns themselves

dropdowns = [Dropdown(440, 5, 60, 25, heroes_options, "Hero"),
             Dropdown(510, 5, 60, 25, spawn_options, "Spawns" ),
             Dropdown(580, 5, 60, 25, team_options, "Teams"),
             Dropdown(650, 5, 60, 25, players_options, "Players")
             ]
 
# Button Class that says when anything defined as a button is pushed things happen
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, active=True):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.active = active
        self.font = pygame.font.Font(None, 32)
    
    def draw(self, screen):
        # Check for mouse hovering over button
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
        
        # To Draw the Button's text
        text_surf = self.font.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    # tuple of the mouse position (x,y)
    def clicked(self, pos):
        return self.rect.collidepoint(pos) and self.active


# Buttons Created
start_button = Button(625, 425, 75, 50, "Start", RED, YELLOW, False)
choose_button = Button(625, 365, 75, 50, "Load", RED, YELLOW, True)
 

# sets Game settings to nothing on start-up
characters_chosen = False

# Heroes List
heroes_list = ["Agarthan Wastebringer",
               "Aquilan Dipped Sword Dancer", 
               "Aquilan Energy Technician",
               "Aquilan Tempest", 
               "Apollonian Grenadier", 
               "Apollonian Swordmaster",
               "Apollonian Tank",
               "Biologic Amplifier",
               "Gothmaug Marauder",
               "Leonid Lieutenant",
               "Leonid Commandant",
               "Leonid Carrier",
               "Iksnkik Hivemind",
               "Molochite All-Mother",
               "Molochite Weapons Tech",
               "Mogwai Mass Mystic",
               "Normanus World-Bearer",
               "Saturni Reaper",
               "Selene Femmentalist",
               "Selene Master Weavemaker",
               "Selene Perfectionist",
               "The Phase Walker",
               "The Spore",
               "Urik La",
               "Urik Mimic",  
               "Urik Ra",
               "Verouk Shadow",
               "Volucris Bullet Beak",
               "Volucris Dart Thrower",
               "Volucris Salter"
               ]


# The Hero Selector Widget
class HeroGrid:
    def __init__(self, x, y, heroes):
        self.x = x
        self.y = y
        self.heroes = heroes
        self.selected = [None] * 4

    def draw(self, screen):
        for i, hero in enumerate(self.heroes):
            pygame.draw.rect(screen, (120, 120, 120), (self.x + (i % 7) * 60, self.y + (i // 7) * 60, 55, 55))

        # How the hero selector handles clicks 
        # team_idx and player_idx confuse me right now
    # What happens on dropdown clicks
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # clicks on dropdowns expand them
            if self.rect.collidepoint(event.pos):
                self.selected.insert(0, "5")
                print( "5")
                return True
            return False


'''     def handle_click(self, pos):
        for i, hero in enumerate (self, heroes_list):
            rect = pygame.Rect(self.x + (i // 4) *50, self.y + (i % 4) * 50, 45, 45)
            if rect.collidepoint(pos):
                self.selected.append(hero)
                return True
        return False  
'''
# The Hero Grid
hero_grid = HeroGrid(0, 0, heroes_list)
    
# Game loop
def main():
    global characters_chosen
    clock = pygame.time.Clock()

    while True:
     
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            

            for dropdown in dropdowns:
                dropdown.handle_event(event)

            # Choose teams button activates start button
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = event.pos

                if start_button.clicked(click_pos) and characters_chosen is False:
                    print("Load game settings first")

                if choose_button.clicked(click_pos):
                    characters_chosen = True
                    start_button.active = True
                    print("It prints.")
                    game_settings = {
                        "heroes": dropdowns[0].current_option,
                        "spawns": dropdowns[1].current_option,
                        "teams": dropdowns[2].current_option,
                        "players": hero_grid.selected
                    }
                
               
                    
                    
            
                elif start_button.clicked(click_pos) and characters_chosen:
                    print("Starting  game with settings: ", game_settings)
                

            

        screen.fill(WHITE) 
        for x in range(0, SCREEN_WIDTH, TILE_SIZE):
            pygame.draw.line(screen, BLACK, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            pygame.draw.line(screen, BLACK, (0, y), (SCREEN_WIDTH, y))
        for dropdown in dropdowns:
            dropdown.draw(screen)
        choose_button.draw(screen)
        if start_button.active is True:
            start_button.draw(screen)
        
        hero_grid.draw(screen)
          

        pygame.display.flip()
        clock.tick(60)
if __name__ == "__main__":
    main()   
        

        

