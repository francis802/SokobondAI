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

# The options in the menu
menu_options = ["start game", "settings", "about", "quit"]
menu_option_selected = 0

# Variable to track if the game has started
game_started = False
gaming = False


# Player position
player_pos = (1,1)
game = None
old_position = (None, None)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if not game_started:
                if event.key in (pygame.K_w, pygame.K_UP):
                    menu_option_selected = (menu_option_selected - 1) % len(menu_options)
                if event.key in (pygame.K_s, pygame.K_DOWN):
                    menu_option_selected = (menu_option_selected + 1) % len(menu_options)
                if event.key == pygame.K_RETURN:  # Press Enter
                    if menu_options[menu_option_selected] == "start game":
                        game_started = True
                        game = model.Game(levels[1], player_pos)
                    elif menu_options[menu_option_selected] == "quit":
                        running = False
            else:
                if event.key in (pygame.K_s, pygame.K_DOWN):
                    controller.movePiece(game, "down")
                if event.key in (pygame.K_w, pygame.K_UP):
                    controller.movePiece(game, "up")
                if event.key in (pygame.K_a, pygame.K_LEFT):
                    controller.movePiece(game, "left")
                if event.key in (pygame.K_d, pygame.K_RIGHT):
                    controller.movePiece(game, "right")
                    

    view.display(screen, game, game_name, game_name_font, menu_options, menu_options_font, menu_option_selected, game_started)         
    
    dt = clock.tick(60) / 1000

pygame.quit()
