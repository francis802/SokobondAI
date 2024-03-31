import pygame

#Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
grey = (128,128,128)
black = (0,0,0)

#Dimensions
SQUARE_SIZE = 80
PIECE_SIZE = 35
CUT_PIECE_SIZE = 8
ELECTRON_SIZE = 8

# Board colors
COLORS = {
    'H': red,
    'N': green,
    'O': blue,
    'C': yellow,
    'y': yellow,
    'g': grey,
    None: white
}


def display(screen, game, game_name, symbol_font, game_name_font, menu_options, menu_options_font, menu_option_selected, game_started, level_option, level_option_selected, level_menu, menu_ia, menu_ia_selected, menu_ia_options, algorithm_menu, algorithm_options, algorithm_selected):
    screen.fill("grey")
    
    if not game_started and not level_menu and not menu_ia and not algorithm_menu: 
        drawMenu(screen, game_name, game_name_font, menu_options, menu_options_font, menu_option_selected)
    elif level_menu:
        drawMenuLevels(screen, game_name, game_name_font, level_option, menu_options_font, level_option_selected)
    elif menu_ia:
        drawMenuIA(screen, game_name, game_name_font, menu_ia_options, menu_options_font, menu_ia_selected)
    elif algorithm_menu:
        drawoptionsIA(screen, game_name, game_name_font, algorithm_options, menu_options_font, algorithm_selected)
    else:
        drawGame(screen, game, symbol_font)

    pygame.display.flip()


def drawMenu(screen, game_name, game_name_font, menu_options, menu_options_font, menu_option_selected):
    # Draw the game name
    game_name_surface = game_name_font.render(game_name, True, "black")
    game_name_pos = game_name_surface.get_rect(midtop=(screen.get_width() // 2, screen.get_height() // 2 - 200))
    screen.blit(game_name_surface, game_name_pos)

    # Draw Menu
    for i, option in enumerate(menu_options):
        option = menu_options_font.render(option, True, "black")
        highlighted = option.get_rect(midtop=(screen.get_width() // 2, screen.get_height() // 2 + i * 50))
        if i == menu_option_selected:
            pygame.draw.rect(screen, "orange", highlighted.inflate(20, 10))  # The rectangle shows in the option selected
        screen.blit(option, highlighted)
    
        

def drawGame(screen, game, symbol_font):
        
        for wall in game.arena.walls:
            pygame.draw.rect(screen, grey, (wall[1] * SQUARE_SIZE, wall[0] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        
        for cut_piece in game.arena.cut_pieces:
            pygame.draw.circle(screen, red, (cut_piece[1] * SQUARE_SIZE, cut_piece[0] * SQUARE_SIZE), CUT_PIECE_SIZE)
            pygame.draw.line(screen, black, (cut_piece[1] * SQUARE_SIZE - 5, cut_piece[0] * SQUARE_SIZE), (cut_piece[1] * SQUARE_SIZE + 5, cut_piece[0] * SQUARE_SIZE), 2)

        for piece in game.pieces:
            for connection in piece.connections:
                pygame.draw.line(screen, (0,0,0), (piece.position[1] * SQUARE_SIZE + SQUARE_SIZE/2, piece.position[0] * SQUARE_SIZE + SQUARE_SIZE/2), (connection.position[1] * SQUARE_SIZE + SQUARE_SIZE/2, connection.position[0] * SQUARE_SIZE + SQUARE_SIZE/2), 5)
        for piece in game.pieces:
            # Draw the piece:
                pygame.draw.circle(screen, COLORS[piece.atom], (piece.position[1] * SQUARE_SIZE + SQUARE_SIZE/2, piece.position[0] * SQUARE_SIZE + SQUARE_SIZE/2), PIECE_SIZE)
                pygame.draw.circle(screen, black, (piece.position[1] * SQUARE_SIZE + SQUARE_SIZE/2, piece.position[0] * SQUARE_SIZE + SQUARE_SIZE/2), PIECE_SIZE, 5)
                text_surface = symbol_font.render(piece.atom, True, (0,0,0))
                text_rect = text_surface.get_rect(center=(piece.position[1] * SQUARE_SIZE + SQUARE_SIZE/2, piece.position[0] * SQUARE_SIZE + SQUARE_SIZE/2))
                screen.blit(text_surface, text_rect)

            # Draw avElectrons:
                for electrons in range(piece.avElectrons):
                    angle = (360 / piece.avElectrons) * electrons
                    # Calcular a posição relativa do elétron de valência em relação ao átomo
                    relative_x = int(pygame.math.Vector2(35, 0).rotate(angle).x)
                    relative_y = int(pygame.math.Vector2(35, 0).rotate(angle).y)
                    # Calcular a posição absoluta do elétron de valência em relação à tela
                    x = piece.position[1] * SQUARE_SIZE + SQUARE_SIZE/2 + relative_x
                    y = piece.position[0] * SQUARE_SIZE + SQUARE_SIZE/2 + relative_y
                    pygame.draw.circle(screen, white, (x , y), ELECTRON_SIZE)
                    pygame.draw.circle(screen, (0,0,0), (x, y), ELECTRON_SIZE, 5)
            
# Menu to select the level
def drawMenuLevels(screen, game_name, game_name_font, level_option, menu_options_font, level_option_selected):
    # Draw the level selection name
    game_name = "Level Selection"
    game_name_surface = game_name_font.render(game_name, True, "black")
    game_name_pos = game_name_surface.get_rect(midtop=(screen.get_width() // 2, screen.get_height() // 2 - 250))
    screen.blit(game_name_surface, game_name_pos)

    #Draw Easy, Medium and Hard text
    larger_font = pygame.font.SysFont("Arial", 36)
    difficulties = ["Easy", "Medium", "Hard", "Very Hard"]
    for i, difficulty in enumerate(difficulties):
        text_surface = larger_font.render(difficulty, True, "black")
        text_pos = text_surface.get_rect(midtop=((2 * i + 1) * screen.get_width() // (len(difficulties) * 2), 350))
        screen.blit(text_surface, text_pos)
            
    # Draw levels 1, 2, and 3 under the "Easy" column
    for i, option in enumerate(level_option[1:4]):
        option_surface = menu_options_font.render(option, True, (0, 0, 0))
        easy_text_rect = text_surface.get_rect(midtop=((2 * difficulties.index("Easy") + 1) * screen.get_width() // (len(difficulties) * 2), 350))
        option_pos = option_surface.get_rect(midtop=(easy_text_rect.centerx, easy_text_rect.bottom + 50 + i * (option_surface.get_height() + 15)))  # Adjust the value 10 for spacing
        screen.blit(option_surface, option_pos)
        if i + 1 == level_option_selected:
            pygame.draw.rect(screen, "orange", option_pos.inflate(20, 10))
            screen.blit(option_surface, option_pos)
            
    # Draw levels 4, 5, and 6 under the "Medium" column
    for i, option in enumerate(level_option[4:7]):
        option_surface = menu_options_font.render(option, True, (0, 0, 0))
        medium_text_rect = text_surface.get_rect(midtop=((2 * difficulties.index("Medium") + 1) * screen.get_width() // (len(difficulties) * 2), 350))
        option_pos = option_surface.get_rect(midtop=(medium_text_rect.centerx, medium_text_rect.bottom + 50 + i * (option_surface.get_height() + 15)))  # Adjust the value 15 for spacing
        screen.blit(option_surface, option_pos)
        # Highlight the selected option
        if i + 4 == level_option_selected:
            pygame.draw.rect(screen, "orange", option_pos.inflate(20, 10))
            screen.blit(option_surface, option_pos)

            
    # Draw levels 7 and 8 under the "Hard" column
    for i, option in enumerate(level_option[7:9]):
        option_surface = menu_options_font.render(option, True, (0, 0, 0))
        hard_text_rect = text_surface.get_rect(midtop=((2 * difficulties.index("Hard") + 1) * screen.get_width() // (len(difficulties) * 2), 350))
        option_pos = option_surface.get_rect(midtop=(hard_text_rect.centerx, hard_text_rect.bottom + 50 + i * (option_surface.get_height() + 15)))  # Adjust the value 15 for spacing
        screen.blit(option_surface, option_pos)
        # Highlight the selected option
        if i + 7 == level_option_selected:  # Adjusted index to match level_option index
            pygame.draw.rect(screen, "orange", option_pos.inflate(20, 10))
            screen.blit(option_surface, option_pos)

    # Draw levels 9 and 10 under the "Very Hard" column
    for i, option in enumerate(level_option[9:11]):  # Adjusted to include level 10
        option_surface = menu_options_font.render(option, True, (0, 0, 0))
        very_hard_text_rect = text_surface.get_rect(midtop=((2 * difficulties.index("Very Hard") + 1) * screen.get_width() // (len(difficulties) * 2), 350))
        option_pos = option_surface.get_rect(midtop=(very_hard_text_rect.centerx, very_hard_text_rect.bottom + 50 + i * (option_surface.get_height() + 15)))  # Adjust the value 15 for spacing
        screen.blit(option_surface, option_pos)
        # Highlight the selected option
        if i + 9 == level_option_selected:  # Adjusted index to match level_option index
            pygame.draw.rect(screen, "orange", option_pos.inflate(20, 10))
            screen.blit(option_surface, option_pos)

    
    
            
            
            
#Menu to select how to play 
def drawMenuIA(screen, game_name, game_name_font, menu_ia_options, menu_options_font, menu_ia_selected):
    # Draw the game name
    game_name_surface = game_name_font.render(game_name, True, "black")
    game_name_pos = game_name_surface.get_rect(midtop=(screen.get_width() // 2, screen.get_height() // 2 - 200))
    screen.blit(game_name_surface, game_name_pos)

    # Draw Menu
    for i, option in enumerate(menu_ia_options):
        option = menu_options_font.render(option, True, "black")
        highlighted = option.get_rect(midtop=(screen.get_width() // 2, screen.get_height() // 2 + i * 50))
        if i == menu_ia_selected:
            pygame.draw.rect(screen, "orange", highlighted.inflate(20, 10))  # The rectangle shows in the option selected
        screen.blit(option, highlighted)
        
        
#Menu to select how to play 
def drawoptionsIA(screen, game_name, game_name_font, algorithm_options, menu_options_font, algorithm_selected):
    # Draw the game name
    game_name_surface = game_name_font.render(game_name, True, "black")
    game_name_pos = game_name_surface.get_rect(midtop=(screen.get_width() // 2, screen.get_height() // 2 - 200))
    screen.blit(game_name_surface, game_name_pos)

    # Draw Options
    for i, option in enumerate(algorithm_options):
        option = menu_options_font.render(option, True, "black")
        highlighted = option.get_rect(midtop=(screen.get_width() // 2, screen.get_height() // 2 + i * 50))
        if i == algorithm_selected:
            pygame.draw.rect(screen, "orange", highlighted.inflate(20, 10))  # The rectangle shows in the option selected
        screen.blit(option, highlighted)


def drawVictory(screen):
    screen.fill("grey")
    victory_text = pygame.font.SysFont("Arial", 100).render("Victory!", True, "black")
    text_rect = victory_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(victory_text, text_rect)
    pygame.display.flip()  
