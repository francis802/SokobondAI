import pygame
import controller
from levels import levels
import view
from model import Game, Arena
from algorythms import DFS, BFS, greedy_search, a_star_search, iterative_deepening_search
import copy

# ATENTION: The y axis is turned upside down, so to go up you have to subtract 1, and add 1 to go down!!!

# pygame setup
pygame.init()
view.init()
clock = pygame.time.Clock()
running = True
dt = 0

# The options in the menu
menu_options = ["start game", "about", "quit"]
menu_option_selected = 0
about = False

#Level Options
level_option = ["","Level 1", "Level 2", "Level 3", "Level 4", "Level 5", "Level 6", "Level 7", "Level 8", "Level 9", "Level 10"]
level_option_selected = 0
level_menu = False

#IA Options
menu_ia_options = ["Play", "IA Play"]
menu_ia_selected = 0
menu_ia = False

#Algorithm Options
algorithm_options = ["DFS", "BFS", "Greedy", "A*", "Iterative Deepening"]
algorithm_selected = 5
algorithm_menu = False

# Variable to track if the game has started
game_started = False

# Player position
game = None
arena = None
prev_states = []
ai_result = 0
ai_done = False
ai_moves = []



def getMoves(state):
    moves = []
    while state.parent != None:
        moves.append(state)
        state = state.parent
    return moves
    

while running:
    # AI: run the AI
    if menu_ia_selected == 1 and game_started and not ai_done: 
            ai_done = True
            if algorithm_selected == 0:
                ai_result = DFS(game)
            elif algorithm_selected == 1:
                ai_result = BFS(game)
            elif algorithm_selected == 2:
                ai_result = greedy_search(game)
            elif algorithm_selected == 3:
                ai_result = a_star_search(game)
            elif algorithm_selected == 4:
                ai_result = iterative_deepening_search(game)
            ai_moves = getMoves(ai_result)
    # AI: handle the AI moves
    if menu_ia_selected == 1 and game_started and ai_done:
        if len(ai_moves) > 0:
            game = ai_moves.pop().state
            pygame.time.delay(1000)
            
    # CONTROLLER: handle the events
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if not game_started and not level_menu and not menu_ia and not algorithm_menu and not about:
                    if event.key in (pygame.K_w, pygame.K_UP):
                        menu_option_selected = (menu_option_selected - 1) % len(menu_options)
                    if event.key in (pygame.K_s, pygame.K_DOWN):
                        menu_option_selected = (menu_option_selected + 1) % len(menu_options)
                    if event.key == pygame.K_RETURN:  
                        if menu_options[menu_option_selected] == "start game":
                            menu_ia = True
                        elif menu_options[menu_option_selected] == "about":
                            about = True
                        elif menu_options[menu_option_selected] == "quit":
                            running = False
                elif about:
                    if event.key == pygame.K_RETURN: 
                        about = False
                elif menu_ia:
                    if event.key in (pygame.K_w, pygame.K_UP):
                        menu_ia_selected = (menu_ia_selected - 1) % len(menu_ia_options)
                    if event.key in (pygame.K_s, pygame.K_DOWN):
                        menu_ia_selected = (menu_ia_selected + 1) % len(menu_ia_options)
                    if event.key == pygame.K_RETURN: 
                        if menu_ia_options[menu_ia_selected] == "Play":
                            level_menu = True
                        elif menu_ia_options[menu_ia_selected] == "IA Play":
                            algorithm_menu = True
                        menu_ia = False
                elif algorithm_menu:
                    if event.key in (pygame.K_w, pygame.K_UP):
                        algorithm_selected = (algorithm_selected - 1) % len(algorithm_options)
                    if event.key in (pygame.K_s, pygame.K_DOWN):
                        algorithm_selected = (algorithm_selected + 1) % len(algorithm_options)
                    if event.key == pygame.K_RETURN: 
                        if algorithm_options[algorithm_selected] == "DFS":
                            level_menu = True
                        elif algorithm_options[algorithm_selected] == "BFS":
                            level_menu = True
                        elif algorithm_options[algorithm_selected] == "Greedy":
                            level_menu = True
                        elif algorithm_options[algorithm_selected] == "A*":
                            level_menu = True
                        elif algorithm_options[algorithm_selected] == "Iterative Deepening":
                            level_menu = True
                        algorithm_menu = False
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
                        elif level_option[level_option_selected] == "Level 6":
                            arena = Arena(levels[6])
                        elif level_option[level_option_selected] == "Level 7":
                            arena = Arena(levels[7])
                        elif level_option[level_option_selected] == "Level 8":
                            arena = Arena(levels[8])
                        elif level_option[level_option_selected] == "Level 9":
                            arena = Arena(levels[9])
                        elif level_option[level_option_selected] == "Level 10":
                            arena = Arena(levels[10])                
                        game = Game(arena)
                        level_menu = False
                        game_started = True
                        prev_states.append(copy.deepcopy(game.pieces))  
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

    # VIEW: display the game
    view.display(game, menu_options, menu_option_selected, game_started, level_option, level_option_selected, level_menu, menu_ia, menu_ia_selected, menu_ia_options, algorithm_menu, algorithm_options, algorithm_selected, about)
    dt = clock.tick(60) / 1000

    # AI LAST MOVE: handle the last move of the AI
    if len(ai_moves) == 0 and menu_ia_selected == 1 and game_started:
            pygame.time.delay(1000)

    # VICTORY: handle the end of the game
    if game_started and controller.endGame(game.pieces):
        view.drawVictory()  
        pygame.display.flip()
        menu_option_selected = 0
        level_option_selected = 0
        level_menu = False
        menu_ia_selected = 0
        menu_ia = False
        algorithm_selected = 5
        algorithm_menu = False
        game_started = False 
        game = None
        arena = None
        prev_states = []
        ai_result = 0
        ai_done = False
        ai_moves = []
        pygame.time.delay(1500)

        
pygame.quit()


