import pygame
import controller
from levels import levels
import view
from model import Game, Arena
from algorythms import DFS, BFS, greedy_search, a_star_search
import copy

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
level_option = ["","Level 1", "Level 2", "Level 3", "Level 4", "Level 5"]
level_option_selected = 0
level_menu = False

#IA Options
menu_ia_options = ["Play", "IA Play"]
menu_ia_selected = 0
menu_ia = False

# Variable to track if the game has started
game_started = False


# Player position
game = None
arena = None
prev_states = []

def printMove():
    print("Moves: [")
    for move in prev_states:
        lista = [(piece.connections.copy(), piece.position) for piece in move.pieces]
        print(",  ", lista)
    print("]")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if not game_started and not level_menu and not menu_ia:
                if event.key in (pygame.K_w, pygame.K_UP):
                    menu_option_selected = (menu_option_selected - 1) % len(menu_options)
                if event.key in (pygame.K_s, pygame.K_DOWN):
                    menu_option_selected = (menu_option_selected + 1) % len(menu_options)
                if event.key == pygame.K_RETURN:  
                    if menu_options[menu_option_selected] == "start game":
                        menu_ia = True
                        #level_menu = True
                        #game_started = True
                        #game = Game(levels[4])
                        #algo = BFS(game)

                        #algo = a_star_search(game)
                        #for piece in algo.state.game.pieces:
                        #   print( piece.position, piece.atom)
                        #    print("Connections:")
                        #    for connection in piece.connections:
                        #        print(" / ", connection.position, connection.atom)
                        #    print("-------------------------------------")
                        #algo.print_solution()

                    elif menu_options[menu_option_selected] == "quit":
                        running = False
            elif menu_ia:
                if event.key in (pygame.K_w, pygame.K_UP):
                    menu_ia_selected = (menu_ia_selected - 1) % len(menu_ia_options)
                if event.key in (pygame.K_s, pygame.K_DOWN):
                    menu_ia_selected = (menu_ia_selected + 1) % len(menu_ia_options)
                if event.key == pygame.K_RETURN: 
                    if menu_ia_options[menu_ia_selected] == "Play":
                        level_menu = True
                    elif menu_ia_options[menu_ia_selected] == "IA Play":
                        level_menu = True
                    menu_ia = False
            elif level_menu:
                if event.key in (pygame.K_w, pygame.K_UP):
                    level_option_selected = (level_option_selected - 1) % len(level_option)
                if event.key in (pygame.K_s, pygame.K_DOWN):
                    level_option_selected = (level_option_selected + 1) % len(level_option)
                if event.key == pygame.K_RETURN and level_option_selected != 0: 
                    if level_option[level_option_selected] == "Level 1":
                        arena = Arena(levels[1])
                    elif level_option[level_option_selected] == "Level 2":
                        arena = Arena(levels[2])
                    elif level_option[level_option_selected] == "Level 3":
                        arena = Arena(levels[3])
                    elif level_option[level_option_selected] == "Level 4":
                        arena = Arena(levels[4])
                    elif level_option[level_option_selected] == "Level 5":
                        arena = Arena(levels[5])
                    game = Game(arena)
                    level_menu = False
                    game_started = True
                    prev_states.append(copy.deepcopy(game.pieces))
                    #algo = a_star_search(game)
                    #algo.print_solution()
                    
            else:
                if event.key in (pygame.K_s, pygame.K_DOWN):
                    controller.movePiece(game, "down", prev_states)
                if event.key in (pygame.K_w, pygame.K_UP):
                    controller.movePiece(game, "up", prev_states)
                if event.key in (pygame.K_a, pygame.K_LEFT):
                    controller.movePiece(game, "left", prev_states)
                if event.key in (pygame.K_d, pygame.K_RIGHT):
                    controller.movePiece(game, "right", prev_states)
                   
                if event.key == pygame.K_r:
                    game = Game(arena)
                if event.key == pygame.K_z:
                    if len(prev_states) > 0:
                        last_state = prev_states.pop()
                        game.pieces = last_state

    
    view.display(screen, game, game_name, symbol_font, game_name_font, menu_options, menu_options_font, menu_option_selected, game_started, level_option, level_option_selected, level_menu, menu_ia, menu_ia_selected, menu_ia_options)
    dt = clock.tick(60) / 1000
    
    if (game_started and controller.endGame(game.pieces)):
        running = False
        break

pygame.quit()


