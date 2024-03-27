import pygame

#Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
grey = (128,128,128)
black = (0,0,0)

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


def display(screen, game, game_name, symbol_font, game_name_font, menu_options, menu_options_font, menu_option_selected, game_started, level_option, level_option_selected, level_menu):
    screen.fill("grey")
    
    if not game_started and not level_menu: 
        drawMenu(screen, game_name, game_name_font, menu_options, menu_options_font, menu_option_selected)
    elif level_menu:
        drawMenuLevels(screen, game_name, game_name_font, level_option, menu_options_font, level_option_selected)
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
        
        for wall in game.walls:
            pygame.draw.rect(screen, grey, (wall[1] * 100, wall[0] * 100, 100, 100))
        
        for cut_piece in game.cut_pieces:
            pygame.draw.circle(screen, red, (cut_piece[1] * 100, cut_piece[0] * 100), 10)
            pygame.draw.line(screen, black, (cut_piece[1] * 100 - 5, cut_piece[0] * 100), (cut_piece[1] * 100 + 5, cut_piece[0] * 100), 2)

        for index, piece in enumerate(game.pieces):
            # Draw connections:
                for connection in piece.connections:
                    pygame.draw.line(screen, (0,0,0), (piece.position[1] * 100 + 50, piece.position[0] * 100 + 50), (connection.position[1] * 100 + 50, connection.position[0] * 100 + 50), 5)    

            # Draw the piece:
                pygame.draw.circle(screen, COLORS[piece.atom], (piece.position[1] * 100 + 50, piece.position[0] * 100 + 50), 40)
                pygame.draw.circle(screen, black, (piece.position[1] * 100 + 50, piece.position[0] * 100 + 50), 40, 5)
                text_surface = symbol_font.render(piece.atom, True, (0,0,0))
                text_rect = text_surface.get_rect(center=(piece.position[1] * 100 + 50, piece.position[0] * 100 + 50))
                screen.blit(text_surface, text_rect)

            # Draw avElectrons:
                for electrons in range(piece.avElectrons):
                    angle = (360 / piece.avElectrons) * electrons
                    # Calcular a posição relativa do elétron de valência em relação ao átomo
                    relative_x = int(pygame.math.Vector2(39, 0).rotate(angle).x)
                    relative_y = int(pygame.math.Vector2(39, 0).rotate(angle).y)
                    # Calcular a posição absoluta do elétron de valência em relação à tela
                    x = piece.position[1] * 100 + 50 + relative_x
                    y = piece.position[0] * 100 + 50 + relative_y
                    pygame.draw.circle(screen, white, (x , y), 10)
                    pygame.draw.circle(screen, (0,0,0), (x, y), 10, 5)
            
# Menu to select the level
def drawMenuLevels(screen, game_name, game_name_font, level_option, menu_options_font, level_option_selected):
    # Draw the level selection name
    game_name = "Level Selection"
    game_name_surface = game_name_font.render(game_name, True, "black")
    game_name_pos = game_name_surface.get_rect(midtop=(screen.get_width() // 2, screen.get_height() // 2 - 250))
    screen.blit(game_name_surface, game_name_pos)

    #Draw Easy, Medium and Hard text
    larger_font = pygame.font.SysFont("Arial", 36)
    easy_text_surface = larger_font.render("Easy", True, "black")
    easy_text_pos = easy_text_surface.get_rect(midtop=(screen.get_width() // 4, 350))
    screen.blit(easy_text_surface, easy_text_pos)

    medium_text_surface = larger_font.render("Medium", True, "black")
    medium_text_pos = medium_text_surface.get_rect(midtop=(screen.get_width() // 2, 350))
    screen.blit(medium_text_surface, medium_text_pos)

    hard_text_surface = larger_font.render("Hard", True, "black")
    hard_text_pos = hard_text_surface.get_rect(midtop=(3 * screen.get_width() // 4, 350))
    screen.blit(hard_text_surface, hard_text_pos)

    # Draw levels 1 and 2
    for i, option in enumerate(level_option[1:3]):
        option_surface = menu_options_font.render(option, True, (0, 0, 0)) 
        option_pos = option_surface.get_rect(midtop=(screen.get_width() // 4, 450 + i * 50))  
        screen.blit(option_surface, option_pos)
        # Highlight the selected option
        if i == level_option_selected:
            pygame.draw.rect(screen,"orange", option_pos.inflate(20, 10))  
            screen.blit(option_surface, option_pos)
            
    # Draw levels 3 and 4
    for i, option in enumerate(level_option[3:5]):
        option_surface = menu_options_font.render(option, True, (0, 0, 0))  
        option_pos = option_surface.get_rect(midtop=(screen.get_width() // 2, 450 + i * 50)) 
        screen.blit(option_surface, option_pos)
        # Highlight the selected option
        if i + 2 == level_option_selected:
            pygame.draw.rect(screen,"orange", option_pos.inflate(20, 10))
            screen.blit(option_surface, option_pos)
            
    # Draw level 5
    for i, option in enumerate(level_option[-1:]):
        option_surface = menu_options_font.render(option, True, (0, 0, 0)) 
        option_pos = option_surface.get_rect(midtop=(3 * screen.get_width() // 4, 450))  
        screen.blit(option_surface, option_pos)
        # Highlight the selected option
        if 5 == level_option_selected + 1:
            pygame.draw.rect(screen,"orange", option_pos.inflate(20, 10))
            screen.blit(option_surface, option_pos)
    
    
    
    
            
            
            
#Menu to select how to play 
def drawMenuIA(screen, game_name, game_name_font, menu_ia, menu_options_font, menu_ia_selected):
    # Draw the game name
    game_name_surface = game_name_font.render(game_name, True, "black")
    game_name_pos = game_name_surface.get_rect(midtop=(screen.get_width() // 2, screen.get_height() // 2 - 200))
    screen.blit(game_name_surface, game_name_pos)

    # Draw Menu
    for i, option in enumerate(menu_ia):
        option = menu_options_font.render(option, True, "black")
        highlighted = option.get_rect(midtop=(screen.get_width() // 2, screen.get_height() // 2 + i * 50))
        if i == menu_ia_selected:
            pygame.draw.rect(screen, "orange", highlighted.inflate(20, 10))  # The rectangle shows in the option selected
        screen.blit(option, highlighted)
