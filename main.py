import pygame
import sys
import random
 
from classes import spawnable_heroes, herocard_decks
#from  classes import  dropdowns, team_options, players_options

'''
# a short program for counting cards, it's jenky but works, change inputs as needed (it's manually driven)
cardcount = 0
name = "Agarthan Wastebringer"
for x in herocard_decks:
    print(name)
    if x[0] != name:
        print(cardcount)
        cardcount = 0
    if x[1] == "combat":
        cardcount += x[3]
    #if x[1] == "special":
       # cardcount += x[4]
    
    name = x[0]
'''
   


# Initialize Pygame
pygame.init()

# Screen settings
GRID_WIDTH, GRID_HEIGHT = 24, 16
TILE_SIZE = 30  # Pixels per tile
SCREEN_WIDTH = GRID_WIDTH * TILE_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * TILE_SIZE

screen = pygame.display.set_mode((SCREEN_WIDTH + 650, SCREEN_HEIGHT +300))

pygame.display.set_caption("Infinite Duels Prototype")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0) 
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLUE_GREEN = (0, 255, 255)
VIOLET = (205, 0, 255)
GRAY = (150, 150, 150) 
LIGHT_GRAY = (200, 200, 200)
GOLD = (180, 150, 25)
HIGHLIGHTGREEN = (0, 255, 0, 128)
# DropDown Class for Dropdown Menus for user input
class Dropdown:
    def __init__(self, x, y, width, height, options, label, active = True):
        self.rect = pygame.Rect(x, y, width, height)
        self.options = options
        self.active = active
        self.label = label
        self.current_option = options[0] # Index of selected options
        self.expanded = False
        self.font = pygame.font.Font(None, 22)
        self.label_surface = self.font.render(label, True, BLACK)

    def draw(self, screen):
        #label
        screen.blit(self.label_surface, (self.rect.x, self.rect.y + 25))
        #main box
        pygame.draw.rect(screen, GOLD, self.rect)
        pygame.draw.rect(screen, RED, self.rect, 2)
        #current selection
        text = self.font.render(str(self.current_option), True, BLACK)
        screen.blit(text, (self.rect.x + 5, self.rect.y + 5))
        #The expanded dropdown
        if self.expanded:
            for i, option in enumerate(self.options):
                rect = pygame.Rect(self.rect.x, self.rect.y + (i + 1) * self.rect.height, self.rect.width, self.rect.height)
                pygame.draw.rect(screen, GOLD, rect)
                pygame.draw.rect(screen, RED, rect, 1)
                text = self.font.render(str(option), True, BLACK)
                screen.blit(text, (rect.x + 5, rect.y + 5))

    # What happens on dropdown clicks
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # clicks on dropdowns expand them
            if self.rect.collidepoint(event.pos):
                self.expanded = not self.expanded
                gamestate.dropdownsexpanded = not gamestate.dropdownsexpanded
            # clicks on things in the expanded dropdown list change the option and close the dropdown
            elif self.expanded:
                for i, option in enumerate(self.options):
                    rect = pygame.Rect(self.rect.x, self.rect.y + (i + 1) * self.rect.height, self.rect.width, self.rect.height)
                    if rect.collidepoint(event.pos):
                        self.current_option = option
                        self.expanded = False
 
# Dropdown Selection Lists  herodropdown is to be deleted for multiselect tool
team_options = [1, 2, 3, 4]
players_options = [1, 2, 3, 4] 
map_options = ["Moloch", "Psyche", "Kyumbani", "Verikov", "Luna", "Boz Fura", "Dividia", "Akham-5", "Agartha", "Urik Prime"] 
spawn_options = ["Corners", "Edges", "Center", "Head-Up", "Leader"] 

# The Dropdowns themselves

dropdowns = [Dropdown(830, 160, 90, 25, map_options, "Map", True),
             Dropdown(830, 5, 90, 25, spawn_options, "Spawns" , True),
             Dropdown(730, 160, 90, 25, team_options, "Teams", True),
             Dropdown(730, 5, 90, 25, players_options, "Players", True)
             ]
 
# Button Class that says when anything defined as a button is pushed things happen
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, active = True):
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
        

class Herobutton:
    def __init__(self, x, y, width, height, text, color, hover_color, active = True, chosen = False):
        #Button display info
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.active = active
        self.chosen = chosen
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





    # tuple of the mouse position (x,y) and clickability
    def clicked(self, pos):
        
        return self.rect.collidepoint(pos) and self.active
        

# Buttons Created
start_button = Button(625, 425, 75, 50, "Start", RED, YELLOW, False)
load_button = Button(625, 365, 75, 50, "Load", RED, YELLOW, True)
hero_button = Button(625, 305, 75, 50, "Hero", RED, YELLOW, True)
draw_button = Button(1030, 1, 75, 50, "Draw", RED, YELLOW, False)
move_button = Button(730, 1, 75, 50, "Move", RED, YELLOW, False)
playcard_button = Button(830, 1, 75, 50, "Card", RED, YELLOW, False)
attack_button = Button(930, 1, 75, 50, "Attack", RED, YELLOW, False)


# sets Game settings to nothing on start-up


# Heroes List
heroes_list = ["Agarthan Wastebringer",
               "Apollonian Grenadier", 
               "Apollonian Swordmaster",
               "Apollonian Tank",
               "Aquilan Dipped Sword Dancer", 
               "Aquilan Energy Technician",
               "Aquilan Tempest", 
               "Biologic Amplifier",
               "Gothmaug Marauder",
               "Iksnik Hivemind",
               "Leonid Carrier",
               "Leonid Commandant",
               "Leonid Lieutenant",
               "Molochite All-Mother",
               "Molochite Quarantine Runner",
               "Molochite Weapons Technician",
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
# List of list with necessary data to create hero select buttons
hero_data = []
hero_butts = []

#Makes Acronyms to Fit Button Size, Not the Best Aesthetic
def first_letter(x):
    words = x.split()
    letters = [word[0] for word in words]
    joined_letters = "".join(letters)
    return joined_letters



# List of buttons for hero selection
for i in heroes_list:
    x = [((0 + heroes_list.index(i)) % 7) * 60, 0 + heroes_list.index(i) // 7 * 60, 55, 55, i, RED, YELLOW, False]
    
    hero_icon = Herobutton(x[0],x[1],x[2],x[3],first_letter(x[4]),x[5],x[6],x[7])
    # The meta list
    hero_butts.append(hero_icon)

    hero_data.append(x)



    
    
    
    
game_data = ["Moloch", 2, 1, "Corners"]

def load_data():
    counter = 0
    for dropdown in dropdowns:
        if counter == 0:
            game_data[0] = dropdown.current_option
        if counter == 1:
            game_data[1] = dropdown.current_option
        if counter == 2:
            game_data[2] = dropdown.current_option
        if counter == 3:
            game_data[3] = dropdown.current_option
        counter += 1


chosen_list =[]
def chose_players():
    count = 0
    for button in hero_butts:
        if button.chosen is True and heroes_list[count] not in chosen_list:
            chosen_list.append(heroes_list[count])
    
        count +=1


    



# A list that takes character names and adds their attributes so they can be spawned in
#These lists could be refactored more intelligently, might not be worth the effort
Attribute_List = []


def ind(input):
    return heroes_list.index(input)



battle_heroes = []
bathero_str = []
bathero_final = []
temp_heroes = []
def start_game():
    #through the use of count we can alter the x variable for 2x2 heroes
    count = 0
    #through the use of y_adjustor we can alter the y variable for 2x2 heroes
    #y adjustor stores the x values where we will need to drop the y value an extra spot
    y_adjustor = []
    for i in chosen_list:
        #(self, 0name, 1x, 2y, 3color, 4size = (1, 1), 5height. 6health = 8000, 7shields = 0, 8movement = 5,
        #                9jump = 2, 10jump_type = "jump", 11clamber = 0, 12attack_range = 1):
        
        bathero_str = [spawnable_heroes[ind(i)][0], count, count, spawnable_heroes[ind(i)][3], spawnable_heroes[ind(i)][4],
                             spawnable_heroes[ind(i)][5],spawnable_heroes[ind(i)][6], spawnable_heroes[ind(i)][7], spawnable_heroes[ind(i)][8], spawnable_heroes[ind(i)][9], spawnable_heroes[ind(i)][10], spawnable_heroes[ind(i)][11], spawnable_heroes[ind(i)][12], True]
        
        if count in y_adjustor:
            temp_heroes = Hero(bathero_str[0], 0 + bathero_str[1] % 24, 0 + (bathero_str[2] //24) + 1, bathero_str[3], bathero_str[4],
                                bathero_str[5],bathero_str[6], bathero_str[7], bathero_str[8], bathero_str[9], bathero_str[10], bathero_str[11], bathero_str[12], True
                                )
            gamestate.hero_locations.append((0 + bathero_str[1] % 24, 0+ bathero_str[2]// 24 +1))
        elif (count - 1) in y_adjustor:
           temp_heroes = Hero(bathero_str[0], 0 + bathero_str[1] % 24, 0 + (bathero_str[2] //24) + 1, bathero_str[3], bathero_str[4],
                                bathero_str[5],bathero_str[6], bathero_str[7], bathero_str[8], bathero_str[9], bathero_str[10], bathero_str[11], bathero_str[12], True
                                )
           gamestate.hero_locations.append((0 + bathero_str[1] % 24, 0 + bathero_str[2] // 24 + 1 ))
        else:
            temp_heroes = Hero(bathero_str[0], 0 + bathero_str[1] % 24, 0 + bathero_str[2] //24, bathero_str[3], bathero_str[4],
                                bathero_str[5],bathero_str[6], bathero_str[7], bathero_str[8], bathero_str[9], bathero_str[10], bathero_str[11],bathero_str[12], True
                                )
        gamestate.hero_locations.append((0 + bathero_str[1] % 24, 0 + bathero_str[2]//24))
        
        
        bathero_final.append(bathero_str)               
        battle_heroes.append(temp_heroes)
        if spawnable_heroes[ind(i)][4] == (2,2):
            y_adjustor.append((count+24))
            gamestate.hero_locations.append((0 + bathero_str[1] % 24,0 + bathero_str[2]// 24 +1))
            gamestate.hero_locations.append((0 + bathero_str[1] % 24 + 1,0 + bathero_str[2]// 24))
            gamestate.hero_locations.append((0 + bathero_str[1] % 24 + 1,0 + bathero_str[2]// 24 + 1))
            count += 2
        else:
            count += 1
    
    gamestate.selected_hero = battle_heroes[0]
    gamestate.selected_heromovement = gamestate.selected_hero.possible_movement()
    gamestate.playercount = len(battle_heroes)
    gamestate.heroes = battle_heroes
    

    tempcount = 0
    for x in gamestate.heroes:
        
        #load em in
        x.init_cards()
        #randomize
        x.shuffle()
        #draw 4
        x.genesis_cards()
        if tempcount == 0:
            gamestate.selected_hero.drawn_cards = x.drawn_cards
            gamestate.selected_hero.undrawn_cards = x.undrawn_cards
        tempcount+=1
        #just here for checking 
        #Needs more for including display objects when the game starts, they aren't made yet.


    
class Hero:
    
    def __init__(self, name, x, y, color, size = (1, 1), height = 1, health = 8000, shields = 0, movement = 5,
                 jump = 2, jump_type = "jump", clamber = 0, attack_range = 1, turn = False):
        
        self.name = name 
        self.x = x
        self.y = y
        self.z = 0 # these are x y and z coordinates, probably need an argument for z instead of this
        self.color = color
        self.size = size #width and height of character measured in tiles
        self.health = health
        self.shields = shields
        self.movement = movement
        self.jump = jump
        self.jump_type = jump_type # This logic can't be done without objects to jump over
        self.clamber = clamber
        self.attack_range = attack_range
        self.turn = turn
        self.drawncards_thisturn = 0
        self.undrawn_cards = [] 
        self.drawn_cards = []
        self.currentlydrawncard = None
        self.height = height
        self.locationhistory = []


    # A list of all possible locations the hero can move to.  Messes up on 2x2's after the first movement
    def possible_movement(self):
        #To figure out the list of possible squares the hero can move to you need their location and their movement range
        max_x = self.x + self.movement
        min_x = self.x - self.movement
        max_y = self.y + self.movement
        min_y = self.y - self.movement
        #Heros cannot move outside the bounds of the map (maybe that would be a cool feature in certain scenarios?)
        if max_x > 24:
            max_x = 24
        if min_x < 0:
            min_x = 0
        if max_y > 16:
            max_y = 16
        if min_y < 0:
            min_y = 0
        x_range = []
        y_range = []
        for i in range(min_x, max_x + 1):
            x_range.append(i)
        for i in range(min_y, max_y + 1):
            y_range.append(i)

        #The list of everywhere they can move is just each possible x paired with each possible y.  Usually these setups are inefficient, I think this is ok
        final_zip = []
        for i in x_range:
            for j in y_range:
                final_zip.append((i,j))
        
        #Remove the heroes current location from the list of hero locations (that way they can choose not to move if they want)
        for i in final_zip:
            if i in gamestate.hero_locations:
                final_zip.remove(i)
        final_zip.append((self.x,self.y))
        #Return this list of possible movements to whoever calls
        return(final_zip)


    #Add the heroes cards to their card list.  They are stored once, with quantity as an attribute.  
    # Here we append for each number of cards 'for y in range x[4]' which is the quantity attribute
    #spc/acti: 5attack, 6double attack, 7defense, 8counterattack, 9damage, 10counterdamage, 11heal, 12burn, 13radiation, 14 trap, 15 trapactivations, 16 specialstuff, 17 standalone, 18 range, 
    def init_cards (self):
        for x in herocard_decks:
            #Action and special cards have the same general format in the file they are stored in, combat cards have 1 less attribute stored.
            #I am all but certain this is the most inefficient part of what I'm doing save for what could be occuring in the draw section (don't blame AI for that either, that's me baby)
            if x[0] == self.name:
                if x[1] == 'special':
                    for y in range(x[4]):
                        self.undrawn_cards.append([x[2], x[1], x[3], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12],  x[13], x[14], x[15], x[16], x[17], x[18]])
                if x[1] == 'action':
                    for y in range(x[4]):
                        self.undrawn_cards.append([x[2], x[1], x[3], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12],  x[13], x[14], x[15], x[16], x[17], x[18]])
                if x[1] == 'combat':
                    for y in range(x[3]):
                        self.undrawn_cards.append([x[0], x[1], x[2], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11],  x[12], x[13], x[14], x[15], x[16], x[17]])


    # Draws the first cards, but before that, shuffles the deck.
    def shuffle (self):
        random.shuffle(self.undrawn_cards)
    

    #Take 4 cards from the undrawn, and shuffled list and put them into the list of drawn cards
    def genesis_cards(self):
        
        for i in range(4):
            self.drawn_cards.append(self.undrawn_cards[0])
            self.undrawn_cards.remove(self.undrawn_cards[0])

    #All draws after the genesis.  They are all individual        
    def draw_card(self):
        
        
        self.drawn_cards.append(self.undrawn_cards[0])
        self.undrawn_cards.remove(self.undrawn_cards[0])
        self.drawncards_thisturn +=1
        
        if self.drawncards_thisturn == 2:
            draw_button.active = False
            move_button.color = YELLOW
        gamestate.selected_hero.drawn_cards = self.drawn_cards
        gamestate.selected_hero.undrawn_cards = self.undrawn_cards

    #The reverse of the draw card function  
    #The fact that I have doubly used variables is kind of shit here.
    def undraw_card(self):
        self.undrawn_cards.insert(0, self.drawn_cards[-1] )
        self.drawn_cards.remove(self.drawn_cards[-1])
        self.drawncards_thisturn -=1
        if self.drawncards_thisturn < 2:
            draw_button.active = True
            herocard_buttons.remove(herocard_buttons[-1])

        #Double variables!!
        gamestate.selected_hero.drawn_cards = self.drawn_cards
        gamestate.selected_hero.undrawn_cards = self.undrawn_cards

    #Moves characters and saves their movement history in case we need it.   
    def move_to(self, new_x, new_y):
        if self.size == (1, 1):
        #Remove the old location
            gamestate.hero_locations.remove((self.x, self.y))
        #Big characters have more than 1 "location"
        elif self.size == (2, 2):
            gamestate.hero_locations.remove((self.x,self.y))
            gamestate.hero_locations.remove((self.x + 1, self.y))
            gamestate.hero_locations.remove((self.x + 1, self.y + 1))
            gamestate.hero_locations.remove((self.x, self.y + 1))
        self.locationhistory.append((self.x, self.y))
        self.x = new_x
        self.y = new_y
        #Add the new locations
        if self.size == (1, 1):
            gamestate.hero_locations.append((self.x,self.y))
        elif self.size == (2, 2):
            gamestate.hero_locations.append((self.x, self.y))
            gamestate.hero_locations.append((self.x + 1, self.y))
            gamestate.hero_locations.append((self.x + 1, self.y + 1))
            gamestate.hero_locations.append((self.x, self.y + 1))
        #Redo the algorithm that blitz the opaque green on squares the hero can move to
        pos_moves()
        #Reset the herox and heroy values (not to be confused with hero.x and hero.y, these are herocardbutton.herox and herocardbutton.heroy)
        for x in herocard_buttons:
            x.herox = self.x
            x.heroy = self.y
         
        
    # Moves characters back to where they were before.  Lists have to use insert not append or the locations and heros do not match.
    def undo_move(self, newtuple):
        if self.size == (1, 1):
            #Remove the old location
            gamestate.hero_locations.remove((self.x, self.y))
        elif self.size == (2, 2):
            #Big characters have more than 1 "location"
            gamestate.hero_locations.remove((self.x, self.y))
            gamestate.hero_locations.remove((self.x + 1, self.y))
            gamestate.hero_locations.remove((self.x, self.y + 1))
            gamestate.hero_locations.remove((self.x + 1, self.y + 1))
        self.x = newtuple[0]
        self.y = newtuple[1]
         #Add the new locations
        if self.size == (1, 1):
            gamestate.hero_locations.insert(gamestate.turncount, (self.x, self.y))
        elif self.size == (2, 2):
            gamestate.hero_locations.insert(gamestate.turncount, (self.x, self.y))
            gamestate.hero_locations.insert(gamestate.turncount, (self.x + 1, self.y))
            gamestate.hero_locations.insert(gamestate.turncount, (self.x, self.y + 1))
            gamestate.hero_locations.insert(gamestate.turncount, (self.x + 1, self.y + 1))
            #Redo the algorithm that blitz the opaque green on squares the hero can move to
        pos_moves()
        #Reset the herox and heroy values (not to be confused with hero.x and hero.y, these are herocardbutton.herox and herocardbutton.heroy)
        if gamestate.herocardbuttons:
            for card in gamestate.herocardbuttons:
                card.in_range()
        
        


        
            

        
               
    def draw(self, screen, tile_size):
        
        pygame.draw.rect(screen, self.color, (self.x * tile_size, self.y * tile_size,
                         self.size[0] * tile_size, self.size[1] * tile_size))
        
       #(self, 0name, 1x, 2y, 3color, 4size = (1, 1), 5height. 6health = 8000, 7shields = 0, 8movement = 5,
        #                9jump = 2, 10jump_type = "jump", 11clamber = 0, 12attack_range = 1):


class Gamestate:
    def __init__ (self):
        self.heroes = []
        self.heronames = []
        self.heroeshealth = []
        self.turncount = 0
        self.phase = "draw"
        self.playercount = 0
        self.turn = 0
        self.active = False
        self.selected_hero = None
        self.target_hero = None
        self.selected_heromovement = []
        self.hero_locations = []
        self.herocardbuttons = []
        self.dropdownsexpanded = False
        self.attacking_cards = []
        self.defending_cards = []
        self.defending_hero = None
        self.defensephase_active = False

        #These are for the gamestate HUD
        self.font = pygame.font.Font(None, 22)
        self.x = 1050
        self.y = 55
        self.width = 300
        self.height = 700
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
        

        



    def draw(self, screen):
        pygame.draw.rect(screen, LIGHT_GRAY, self.rect)
        count = 0

        
        
        for hero in battle_heroes:
            cardnumber_surf = self.font.render(str(len(hero.drawn_cards)), True, RED)
            cardnumber_rect = cardnumber_surf.get_rect(topleft=(self.rect.x + 10 + (75 * (count % 4)), self.rect.y + 5 + 50 * (count // 4)))
            name_surf = self.font.render(str(first_letter(hero.name)), True, BLACK)
            name_rect = name_surf.get_rect(topleft=(self.rect.x + 25 + (75 * (count % 4)), self.rect.y + 5 + 50 * (count // 4)))
            health_surf = self.font.render(str(hero.health), True, BLACK)
            health_rect = health_surf.get_rect(topleft=(self.rect.x + 25 + (75 * (count % 4)), self.rect.y + 25 + 50 * (count // 4)))
            screen.blit(name_surf, name_rect)
            screen.blit(health_surf, health_rect)
            screen.blit(cardnumber_surf, cardnumber_rect)
            count += 1

 

gamestate = Gamestate() 


#This seems like a good example of how you can tello Brick is new at programming, cannot be deleted, but why is it there in the first place?
def pos_moves():
    gamestate.selected_heromovement = gamestate.selected_hero.possible_movement()   

cardtype = []
cardtext = []
zipcardtypetext = []



# Generates the initial 4 cards for the selected hero
def generate_cards (hero):
    count = 0
    for x in hero.drawn_cards:
        #There's probably a more pythonic way to do this, pretty sure I save variables multiple times unnecessarily. 
        name = x[0]
        #I don't think I ever use the type variable
        type = x[1]
        text = x[2]
        attack = x[3]
        doubleattack = x[4]
        defense = x[5]
        counterattack = x[6]
        damage = x[7]
        counterdamage = x[8]
        heal = x[9]
        burn = x[10]
        radiation = x[11]
        trap = x[12]
        trapactivations = x[13]
        specialstuff = x[14]
        standalone = x[15]
        range = x[16]

       
        #Do these do anything?  I'm not sure
        cardtype.append(type)
        cardtext.append(text)
        #Draws out the first seven carrds at the bottom of the screen (that's all that fits)
        if count <= 6:
            card_button = Herocardbutton((((0 + count) % 7  * 150)), 550 - ((0 + count) // 7)*245, 146, 219, name, RED, YELLOW, text, True )
            card_button.attack =  attack
            card_button.doubleattack = doubleattack
            card_button.defense = defense
            card_button.counterattack = counterattack
            card_button.damage = damage
            card_button.counterdamage = counterdamage
            card_button.heal = heal
            card_button.burn = burn
            card_button.radiation = radiation
            card_button.trap = trap
            card_button.trapactivations = trapactivations
            card_button.specialstuff = specialstuff
            card_button.standalone = standalone
            card_button.range = range[0]
            card_button.type = type
        
        #Draws out the rest of the cards in groups of three in space at the sides of the board, sort of unnecessary unless you set the original gensis amount higher, sue me
        else:
            card_button = Herocardbutton((((count-7) % 2  * 150+750)), 550 - (0 + (count-5)) // 2 *245, 146, 219, name, RED, YELLOW, text, True )
            card_button.attack =  attack
            card_button.doubleattack = doubleattack
            card_button.defense = defense
            card_button.counterattack = counterattack
            card_button.damage = damage
            card_button.counterdamage = counterdamage
            card_button.heal = heal
            card_button.burn = burn
            card_button.radiation = radiation
            card_button.trap = trap
            card_button.trapactivations = trapactivations
            card_button.specialstuff = specialstuff
            card_button.standalone = standalone
            card_button.range = range[0]
            card_button.type = type
       #Updates everything in gamestate so that it will draw correctly
        count += 1
        
        herocard_buttons.append(card_button)
        card_button.in_range()
        
        gamestate.herocardbuttons = herocard_buttons
        for cards in gamestate.herocardbuttons:
            cards.wrap_text()
        

# Generates cards after being drawn, matching the correct entries and variables is a bit of a nightmare at the moment.  Sue me
def generatedrawn_cards ():
    #Initiates the count at the computer version of the number 4, "3", since we have already drawn 3 cards
    count = 3 + gamestate.selected_hero.drawncards_thisturn

    #Another good example of Brick as a noob, seems like a lot of waste here, its running right now though, sue me.
    gamestate.selected_hero.currentlydrawncard = gamestate.selected_hero.undrawn_cards[0]
    
    name = gamestate.selected_hero.currentlydrawncard[0]
    type = gamestate.selected_hero.currentlydrawncard[1]
    text = gamestate.selected_hero.currentlydrawncard[2]

    attack = gamestate.selected_hero.currentlydrawncard[3]
    doubleattack = gamestate.selected_hero.currentlydrawncard[4]
    defense = gamestate.selected_hero.currentlydrawncard[5]
    counterattack = gamestate.selected_hero.currentlydrawncard[6]
    damage = gamestate.selected_hero.currentlydrawncard[7]
    counterdamage = gamestate.selected_hero.currentlydrawncard[8]
    heal = gamestate.selected_hero.currentlydrawncard[9]
    burn = gamestate.selected_hero.currentlydrawncard[10]
    radiation = gamestate.selected_hero.currentlydrawncard[11]
    trap = gamestate.selected_hero.currentlydrawncard[12]
    trapactivations = gamestate.selected_hero.currentlydrawncard[13]
    specialstuff = gamestate.selected_hero.currentlydrawncard[14]
    standalone = gamestate.selected_hero.currentlydrawncard[15]
    range = gamestate.selected_hero.currentlydrawncard[16]

  


    #comb: 3attack, 4double attack, 5defense, 6counterattack, 7damage, 8counterdamage, 9heal, 10burn, 11radiation, 12 trap, 13 trapactivations, 14 specialstuff, 15 standalone, 16 range
    #spc/att:   4attack, 5double attack, 6defense, 7counterattack, 8damage, 9counterdamage, 10heal, 11burn, 12radiation, 13 trap, 14 trap activation, 15 specialstuff, 17 standalone, 18 range   
   
    #At least I got rid of the for loop since we are dealing with cards drawn (or undrawn) individually now
    if count <= 6:
            card_button = Herocardbutton((((0 + count) % 7  * 150)), 550 - ((0 + count) // 7)*245, 146, 219, name, RED, YELLOW, text, True)
            card_button.attack =  attack
            card_button.doubleattack = doubleattack
            card_button.defense = defense
            card_button.counterattack = counterattack
            card_button.damage = damage
            card_button.counterdamage = counterdamage
            card_button.heal = heal
            card_button.burn = burn
            card_button.radiation = radiation
            card_button.trap = trap
            card_button.trapactivations = trapactivations
            card_button.specialstuff = specialstuff
            card_button.standalone = standalone
            card_button.range = range[0]
            card_button.type = type
    #Draws drawn cards after the count is greater than 8 up the side    
    else:
        card_button = Herocardbutton((((count-7) % 2  * 150+750)), 550 - (0 + (count-5)) // 2 *245, 146, 219, name, RED, YELLOW, text, True)
        card_button.attack =  attack
        card_button.doubleattack = doubleattack
        card_button.defense = defense
        card_button.counterattack = counterattack
        card_button.damage = damage
        card_button.counterdamage = counterdamage
        card_button.heal = heal
        card_button.burn = burn
        card_button.radiation = radiation
        card_button.trap = trap
        card_button.trapactivations = trapactivations
        card_button.specialstuff = specialstuff
        card_button.standalone = standalone
        card_button.range = range[0]
        card_button.type = type
    #check whether cards are in range after they are drawn
    card_button.in_range()
    count += 1
    card_button.wrap_text()
    herocard_buttons.append(card_button)
    
    
    gamestate.herocardbuttons = herocard_buttons
    
    

#Function for making card buttons.  Needs its own cardbutton class
herocard_buttons = []
class Herocardbutton:
    def __init__(self, x, y, width, height, title, color, hover_color, text , active = False, inspect = False):
        self.rect = pygame.Rect(x, y, width, height)
        self.title = title
        self.color = color
        self.hover_color = hover_color
        self.active = active
        # Inspect is just for whether they are reading the card text or title.  Inspect false is the title
        self.inspect = inspect
        self.font = pygame.font.Font(None, 20)
        self.actionfont = pygame.font.Font(None, 40)
        self.bigfont = pygame.font.Font(None, 32)
        self.text = text
        self.width = width
        self.wrappedtitle = None
        self.wrappedtext = None
        self.wrappedtitleheight = 0
        self.wrappedtextheight = 0
        self.titlelinesize = 0
        self.textlinesize = 0
        self.actionlinesize = 0
        self.type = None

        #Card logic info
        self.attack = None
        self.doubleattack = None
        self.defense = None
        self.counterattack = None
        self.damage = None
        self.counterdamage = None
        self.heal = None
        self.burn = None
        self.radiation = None
        self.trap = False
        self.trapactivations = None
        self.specialstuff = False
        self.standalone = False
        self.range = 1
        self.herox = gamestate.selected_hero.x 
        self.heroy = gamestate.selected_hero.y
        self.inrange = False
        self.actions = 2
        self.attackpossibilities = []
        self.availableforplay = False
        self.selectedforplay = False

        #not included in the card lists, just for activating cards on and off
        self.playable = False
        
    def in_range(self):
        #To determine where you can attack you need where the heros are (minus yourself) and your attack range.
        locations = []
        for x in gamestate.hero_locations:
            locations.append(x)
        
        
        possibleattacks = []
        self.herox = gamestate.selected_hero.x
        self.heroy = gamestate.selected_hero.y
        
        #Attack range cannot exceed the bounds of the map, readjust for the range function by adding 1
        max_x = self.herox + (self.range )
        min_x = self.herox - (self.range )
        if max_x >=24:
            max_x = 24
        if min_x <= 0:
            min_x = 0
        max_y = self.heroy + (self.range )
        min_y = self.heroy - (self.range )
        if max_y >=24:
            max_y = 24
        if min_y <= 0:
            min_y = 0
        
        for x in range(min_x, max_x + 1) :
            for y in range(min_y, max_y + 1):
                possibleattacks.append((x,y))
        
        #Ensure your own location is accurate at the last possible second 
        self_loc = ((self.herox, self.heroy))
        
        if self_loc in locations:
            locations.remove(self_loc)
        attackpossibilities = []
        #Get the intersection of possible squares to attack and squares that have heroes in them (that aren't you)
        attackpossibilities = list(set(possibleattacks) & set(locations))
        print(attackpossibilities, gamestate.hero_locations)
        
        #If the list of attack possibilities is empty (this reads if the list does not exist, the button color is red)
        
        
        #If a list of attack possibilities for the card does exist that means the card is in range, set it to true, change the color
        if gamestate.defensephase_active is True:
            if self.type == "combat":
                self.inrange = True
                self.color = VIOLET
        elif attackpossibilities:
            self.color = GOLD
            self.inrange = True
            self.attackpossibilities = attackpossibilities
        else:
            self.color = RED



    #The next algorithm to finish, a big daddy of sorts.
    def play_simplecard(self):
        
        target = gamestate.target_hero
        if self.actions <= 0:
            print("Out of actions sonny")
        elif self.inrange is False:
            print ("Can't play that card")
        elif self.type == "combat":
            attack = 0
            defense = 0
                    
                    
            for x in gamestate.attacking_cards:
                
                attack += x.attack
           
            for x in gamestate.defending_cards:
                defense += x.defense
            damage = attack - defense
            if damage <= 0:
                damage = 0

            gamestate.defending_hero.health -= damage

            playcard_button.color = RED
            #Resets everything to zero for multiple clicks, this won't be useful in future
            gamestate.attacking_cards = []
            gamestate.defending_cards = []
            defense = 0
            damage = 0
            attack = 0
            self.selectedforplay = True
            
        else:
            print("special and action cards are hard.")         
            
        # I will need a targetting algorithm using (self is herocard) self.attackpossibilities and gamestate.hero_locations
    def target_hero(self, grid_x, grid_y):
        for hero in battle_heroes:
            if (hero.x, hero.y) == (grid_x, grid_y):
                gamestate.defending_hero = hero
                gamestate.defensephase_active = True
                for herocard in herocard_buttons:
                    herocard.active = False
                generate_cards(gamestate.defending_hero)
    
    

            

    




    

    

        

        

#AI shit I don't fully understand.  Basically pretends to write it once so it can measure it.
    def wrap_text(self):
        splittitle = self.title.split(' ')
        titlelinesize = self.bigfont.get_linesize()
        textlinesize = self.font.get_linesize()
        actionlinesize = self.actionfont.get_linesize()
        self.titlelinesize = titlelinesize
        self.textlinesize = textlinesize
        self.actionlinesize = actionlinesize
        lines = []
        current_line = []
        current_width = 0


        for word in splittitle:
            word_surface = self.bigfont.render(word, True, BLACK, GOLD)
            word_width = word_surface.get_width()
            if current_width + word_width <= (self.width -5):
                current_line.append(word)
                current_width += word_width + self.bigfont.size(' ')[0]
                
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
                current_width = word_width
        if current_line:
            lines.append(' '.join(current_line))
        self.wrappedtitle = lines
        self.wrappedtitleheight = len(self.wrappedtitle)*titlelinesize
        

        splittext = self.text.split(' ')
        textlines = []
        textcurrentline = []
        current_width = 0
        if self.title == gamestate.selected_hero.name:
            for word in splittext:
                word_surface = self.actionfont.render(word, True, BLACK, GOLD)
                word_width = word_surface.get_width()
                if current_width + word_width <= (self.width-5):
                    textcurrentline.append(word)
                    current_width += word_width + self.actionfont.size(' ')[0]
                else:
                    textlines.append(' '.join(textcurrentline))
                    textcurrentline = [word]
                    current_width = word_width
            if textcurrentline:
                textlines.append(' '.join(textcurrentline))
            self.wrappedtext = textlines
            self.wrappedtextheight = len(self.wrappedtext) * actionlinesize
            
        
        else:
        
            for word in splittext:
                word_surface = self.font.render(word, True, BLACK, GOLD)
                word_width = word_surface.get_width()
                if current_width + word_width <= (self.width-5):
                    textcurrentline.append(word)
                    current_width += word_width + self.font.size(' ')[0]
                else:
                    textlines.append(' '.join(textcurrentline))
                    textcurrentline = [word]
                    current_width = word_width
            if textcurrentline:
                textlines.append(' '.join(textcurrentline))
            self.wrappedtext = textlines
            self.wrappedtextheight = len(self.wrappedtext) * textlinesize
       
        
       
        
        

    
        

    
    
    def draw(self, screen):
        

        # Check for mouse hovering over button
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
        textstart_y = self.rect.y + 20
        titlestart_y = self.rect.y + 20       
        # To Draw the Button's text changing the text back and forth from the title
        if self.inspect is False:
            for i, line in enumerate(self.wrappedtitle):

                text_surf = self.bigfont.render(line, True, BLACK)
                text_rect = text_surf.get_rect(center=(self.rect.centerx, titlestart_y + i * self.titlelinesize))
                
                screen.blit(text_surf, text_rect)
            #text_surf = self.bigfont.render(self.title, True, BLACK)
        else:
            
            for i, line in enumerate(self.wrappedtext):
                if self.type == "combat":
                    text_surf = self.actionfont.render(line, True, BLACK)
                    text_rect = text_surf.get_rect(center=(self.rect.centerx, titlestart_y + i * self.actionlinesize))
                
                else:
                    text_surf = self.font.render(line, True, BLACK)
                    text_rect = text_surf.get_rect(center=(self.rect.centerx, textstart_y + i * self.textlinesize))

                screen.blit(text_surf, text_rect)



            #text_surf = self.font.render(self.text, True, BLACK)
            #text_rect = text_surf.get_rect(center=self.rect.center)
            #screen.blit(text_surf, text_rect)
           #cardname = 
           #card_button = )725, 25, 75, 50, "Attack", RED, YELLOW, False)

    
    # tuple of the mouse position (x,y) and clickability
    def clicked(self, pos):
        
        return self.rect.collidepoint(pos) and self.active

    # The Hero Grid
    #hero_grid = HeroGrid(0, 0, 65, 65, RED, YELLOW, heroes_list)
    
    #characters chosen should go probably, idk what it is
    characters_chosen = False
def ret_xy(click_pos):                         
    mouse_x, mouse_y = click_pos
    grid_x = mouse_x // TILE_SIZE
    grid_y = mouse_y // TILE_SIZE
    return (grid_x, grid_y)
    # Game loop
def main():
    global characters_chosen
    clock = pygame.time.Clock()

    while True:
     
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Dropdowns need updated with reactivity, they don't make functional sense if you look at them
            for dropdown in dropdowns:
                dropdown.handle_event(event)


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for herocard in herocard_buttons:
                        herocard.inspect = not herocard.inspect
                if event.key == pygame.K_d:
                    if playcard_button.color != GREEN:
                        gamestate.heroes[gamestate.turn].draw_card()
                        generatedrawn_cards()


            # Choose teams button activates start button
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = event.pos

               

                if load_button.clicked(click_pos):
                    
                    # Loads the start button on screen
                    start_button.active = True
                    characters_chosen = True
                    load_button.color = GREEN
                    load_data()
                    print(game_data)

                # Turns hero buttons off if they are chosen and adds them to the list of chosen players. Currently no way to get off the chosen list
                for button in hero_butts:
                    if button.clicked(click_pos):
                        button.active = False
                        button.chosen = True
                        chose_players()

                # This is the button that loads in the hero multi select tool.  It remembers buttons that have been chosen.
                if hero_button.clicked(click_pos):
                    for button in hero_butts:
                        if button.chosen is False:
                            button.active = not button.active
                 
                                     
                #Removes buttons from the screen when the start button is pushed
                if start_button.clicked(click_pos):
                    load_button.active = False
                    hero_button.active = False
                    start_button.active = False

                    # Adds the gamestate buttons and starts the gamestate
                    move_button.active = True
                    playcard_button.active = True
                    draw_button.active = True
                    attack_button.active = True
                    gamestate.active = True
                    for button in hero_butts:
                        button.active = False
                    for dropdown in dropdowns:
                        dropdown.active = False
                    
                    #Generates a bunch of shit.  All of the shit probably.
                    start_game()

                    #Initializes the card objects
                    generate_cards(gamestate.selected_hero)
                    
                    

              
   
                        
                #Draws cards, with a limit of 2.  Moving is possible afterwards once the move button is pressed.    
                if draw_button.clicked(click_pos):
                    if playcard_button.color != GREEN:
                        gamestate.heroes[gamestate.turn].draw_card()
                        generatedrawn_cards()
                    
                    #Reactivates the cards / it does this to every card every time.  This will cause issues down the line, I know it.
                    
                    
                #  Move button is a little different.  Changes color a lot, needs an undo move button (probably just change title of move button after the move)   
                if move_button.clicked(click_pos):
                    if playcard_button.color is GREEN:
                        print ("can't move now sonny")
                    else:
                        move_button.color = GREEN
                        move_button.hover_color = BLUE
                if move_button.color == GREEN and move_button.active is True:
                    mouse_x, mouse_y = click_pos
                    grid_x = mouse_x // TILE_SIZE
                    grid_y = mouse_y // TILE_SIZE
                    if (grid_x, grid_y) in gamestate.heroes[gamestate.turn].possible_movement():
                        gamestate.heroes[gamestate.turn].move_to(grid_x, grid_y)
                        battle_heroes[gamestate.turn].x = grid_x
                        battle_heroes[gamestate.turn].y = grid_y
                        move_button.active = False
                
                        for x in gamestate.herocardbuttons:
                            x.in_range()
                                # Changes whether you see the title or text of your cards.  Clicking cards after the play card button will begin the card activation process.
                for herocardbutton in herocard_buttons:
                    if (herocardbutton.color is WHITE and gamestate.defensephase_active is False):
                            mouse_x, mouse_y = click_pos
                            grid_x = mouse_x // TILE_SIZE
                            grid_y = mouse_y // TILE_SIZE
                            herocardbutton.target_hero(grid_x, grid_y)
                           
                    if herocardbutton.clicked(click_pos):
                        if herocardbutton.color is RED:
                            herocardbutton.inspect = not herocardbutton.inspect
                        elif herocardbutton.color is GOLD:
                            herocardbutton.inspect = not herocardbutton.inspect
                        elif herocardbutton.color is ORANGE:
                            if gamestate.defensephase_active is not True:
                                gamestate.attacking_cards.append(herocardbutton)
                            if gamestate.defensephase_active is True:
                                gamestate.defending_cards.append(herocardbutton)
                                herocardbutton.play_simplecard()
                            
                            herocardbutton.color = WHITE      


                        else:
                            herocardbutton.color = ORANGE
                        
                
                
                
                   
                        
                if playcard_button.clicked(click_pos):
                    for card in herocard_buttons:
                        if card.inrange:
                            card.availableforplay = not card.availableforplay
                            
                            if card.availableforplay:
                                card.color = VIOLET
                                playcard_button.color = GREEN
                            else:
                                card.color = GOLD
                                playcard_button.color = RED
                       
                if (event.button == 3 and gamestate.dropdownsexpanded is False):
                    if not load_button.color is GREEN :
                        if (gamestate.active is False):
                            if chosen_list:
                                for button in hero_butts:
                                    if first_letter(chosen_list[-1]) == button.text:
                                        button.active = True
                                chosen_list.remove(chosen_list[-1])

                    if (gamestate.active is True):
                        if ((draw_button.color is GREEN) and ((gamestate.selected_hero.drawncards_thisturn >= 1) and (move_button.color is not GREEN) and (playcard_button.color is not GREEN))):
                            gamestate.selected_hero.undraw_card()
                        if ((draw_button.color is GREEN) and ((playcard_button.active is not True) or (playcard_button.color is GREEN))):
                            for herocardbutton in herocard_buttons:
                                herocardbutton.color = VIOLET
                                if gamestate.defensephase_active is not True:
                                    gamestate.attacking_cards = []
                        for herocard in herocard_buttons:
                            if herocard.selectedforplay is True:
                                herocard.selectedforplay = not herocard.selectedforplay
                                herocard.color = ORANGE


                        if move_button.active is False:
                            if (gamestate.heroes[gamestate.turn].locationhistory and playcard_button.color is not GREEN):
                                gamestate.selected_hero.undo_move(gamestate.heroes[gamestate.turn].locationhistory[-1])
                                move_button.active = True




                    
                    
                    



                            
                            
                            
        
                                
                            
                          


                
                    
                    
                    


                    
                

            

        
        # A surface for highlights, the color is kind of ugly    
        highlight_surface = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
        highlight_surface.fill(HIGHLIGHTGREEN)

        #The white background behind everything.
        screen.fill(WHITE) 
        
        #The ordering on this is super important, I just kind of threw everything together.  If I change it now, undoubtedly different aspects of the program will change.
        for hero in battle_heroes:
            hero.draw(screen, TILE_SIZE)

        #The GridMap
        for x in range(0, SCREEN_WIDTH + 1, TILE_SIZE):
            pygame.draw.line(screen, BLACK, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT + 1, TILE_SIZE):
            pygame.draw.line(screen, BLACK, (0, y), (SCREEN_WIDTH, y))


        for dropdown in dropdowns:
            if dropdown.active is True:
                dropdown.draw(screen)
                    
        for herobutton in hero_butts:
            if herobutton.active is True:
                herobutton.draw(screen)

        #hero-_card buttons are drawn from the herocard_button list.  This is a bit odd admittedly
        for x in herocard_buttons:
            if x.active is True:
                x.draw(screen)
        
            #This the hero select grid               
        if load_button.active is True:
            load_button.draw(screen)
        # This is the button to load and hide the hero select grid
        if hero_button.active is True:
            hero_button.draw(screen)
        if start_button.active is True:
            start_button.draw(screen)
        if playcard_button.active is True:
            playcard_button.draw(screen)
        if draw_button.active is True:
            draw_button.draw(screen)
            draw_button.color = GREEN
        if attack_button.active is True:
            attack_button.draw(screen)
        if move_button.active is True:
            move_button.draw(screen)
        if gamestate.active is True:
            gamestate.draw(screen)
            for (x, y) in gamestate.selected_heromovement:
                if (x, y) not in gamestate.hero_locations:
                    screen.blit(highlight_surface, (x * TILE_SIZE, y * TILE_SIZE))
        
            
        
            
        
        
        
          

        pygame.display.flip()
        clock.tick(60)
if __name__ == "__main__":
    main()   
        

        

