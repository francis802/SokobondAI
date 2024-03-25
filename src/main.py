import pygame
from levels import levels
import view
import model
import controller

# ATENTION: The y axis is turned upside down, so to go up you have to subtract 1, and add 1 to go down!!!

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# Game Name
game_name = "SOKOBOND"



# Fonts
game_name_font = pygame.font.SysFont("Arial", 100)
menu_options_font = pygame.font.SysFont("Arial", 24)
symbol_font = pygame.font.SysFont("Arial", 50)


# The options in the menu
menu_options = ["start game", "settings", "about", "quit"]
menu_option_selected = 0

#Level Options
level_option = ["Level 1", "Level 2", "Level 3", "Level 4", "Level 5"]
level_option_selected = 0
level_menu = False

# Variable to track if the game has started
game_started = False


# Player position
game = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if not game_started and not level_menu:
                if event.key in (pygame.K_w, pygame.K_UP):
                    menu_option_selected = (menu_option_selected - 1) % len(menu_options)
                if event.key in (pygame.K_s, pygame.K_DOWN):
                    menu_option_selected = (menu_option_selected + 1) % len(menu_options)
                if event.key == pygame.K_RETURN:  # Press Enter
                    if menu_options[menu_option_selected] == "start game":
                        level_menu = True
                    elif menu_options[menu_option_selected] == "quit":
                        running = False
            if level_menu:
                if event.key in (pygame.K_w, pygame.K_UP):
                    level_option_selected = (level_option_selected - 1) % len(level_option)
                if event.key in (pygame.K_s, pygame.K_DOWN):
                    level_option_selected = (level_option_selected + 1) % len(level_option)
                if event.key == pygame.K_RETURN:  # Press Enter
                    if level_option[level_option_selected] == "Level 1":
                        game_started = True
                        game = model.Game(levels[1]) 
                    elif level_option[level_option_selected] == "Level 2":
                        game_started = True
                        game = model.Game(levels[2]) 
                    elif level_option[level_option_selected] == "Level 3":
                        game_started = True
                        game = model.Game(levels[3]) 
                    elif level_option[level_option_selected] == "Level 4":
                        game_started = True
                        game = model.Game(levels[4])
                    elif level_option[level_option_selected] == "Level 5":
                        game_started = True
                        game = model.Game(levels[5])  
            else:
                if event.key in (pygame.K_s, pygame.K_DOWN):
                    controller.movePiece(game, "down")
                if event.key in (pygame.K_w, pygame.K_UP):
                    controller.movePiece(game, "up")
                if event.key in (pygame.K_a, pygame.K_LEFT):
                    controller.movePiece(game, "left")
                if event.key in (pygame.K_d, pygame.K_RIGHT):
                    controller.movePiece(game, "right")

    view.display(screen, game, game_name, symbol_font, game_name_font, menu_options, menu_options_font, menu_option_selected, game_started, level_option, level_option_selected, level_menu )
    
    dt = clock.tick(60) / 1000
    
    if (game_started and controller.endGame(game)):
        running = False
        break

pygame.quit()
