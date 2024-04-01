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

# Declaração das variáveis globais
screen = None
game_name = "SOKOBOND"
game_name_font = None
menu_options_font = None
symbol_font = None

def init():
    # Declarando as variáveis globais dentro da função
    global screen
    global game_name_font
    global menu_options_font
    global symbol_font

    # Definindo os valores das variáveis
    screen = pygame.display.set_mode((1280, 720))
    game_name_font = pygame.font.SysFont("Arial", 100)
    menu_options_font = pygame.font.SysFont("Arial", 24)
    symbol_font = pygame.font.SysFont("Arial", 50)

def display(game, menu_options, menu_option_selected, game_started, level_option, level_option_selected, level_menu, menu_ia, menu_ia_selected, menu_ia_options, algorithm_menu, algorithm_options, algorithm_selected, about):
    screen.fill("grey")
    
    if not game_started and not level_menu and not menu_ia and not algorithm_menu: 
        drawMenu(menu_options, menu_option_selected)
    elif level_menu:
        drawMenuLevels(level_option, level_option_selected)
    elif menu_ia:
        drawMenuIA(menu_ia_options, menu_ia_selected)
    elif algorithm_menu:
        drawoptionsIA(algorithm_options, algorithm_selected)
    elif game_started:
        drawGame(game)

    if about:
        drawAbout()

    pygame.display.flip()


def drawMenu(menu_options, menu_option_selected):
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
    
        

def drawGame(game):
       # Calcula o tamanho do tabuleiro com base nas dimensões do tabuleiro e na proporção do tamanho dos quadrados
    board_width = len(game.arena.board[0]) * SQUARE_SIZE
    board_height = len(game.arena.board) * SQUARE_SIZE

    # Calcula o deslocamento necessário para centralizar o tabuleiro
    horizontal_offset = (screen.get_width() - board_width) // 2
    vertical_offset = (screen.get_height() - board_height) // 2

    for wall in game.arena.walls:
        pygame.draw.rect(screen, grey, (wall[1] * SQUARE_SIZE + horizontal_offset, wall[0] * SQUARE_SIZE + vertical_offset, SQUARE_SIZE, SQUARE_SIZE))

    for cut_piece in game.arena.cut_pieces:
        pygame.draw.circle(screen, red, (cut_piece[1] * SQUARE_SIZE + horizontal_offset, cut_piece[0] * SQUARE_SIZE + vertical_offset), CUT_PIECE_SIZE)
        pygame.draw.line(screen, black, (cut_piece[1] * SQUARE_SIZE - 5 + horizontal_offset, cut_piece[0] * SQUARE_SIZE + vertical_offset), (cut_piece[1] * SQUARE_SIZE + 5 + horizontal_offset, cut_piece[0] * SQUARE_SIZE + vertical_offset), 2)

    for piece in game.pieces:
        for connection in piece.connections:
            pygame.draw.line(screen, (0,0,0), (piece.position[1] * SQUARE_SIZE + SQUARE_SIZE/2 + horizontal_offset, piece.position[0] * SQUARE_SIZE + SQUARE_SIZE/2 + vertical_offset), (connection.position[1] * SQUARE_SIZE + SQUARE_SIZE/2 + horizontal_offset, connection.position[0] * SQUARE_SIZE + SQUARE_SIZE/2 + vertical_offset), 5)
    for piece in game.pieces:
        # Desenha a peça:
        pygame.draw.circle(screen, COLORS[piece.atom], (piece.position[1] * SQUARE_SIZE + SQUARE_SIZE/2 + horizontal_offset, piece.position[0] * SQUARE_SIZE + SQUARE_SIZE/2 + vertical_offset), PIECE_SIZE)
        pygame.draw.circle(screen, black, (piece.position[1] * SQUARE_SIZE + SQUARE_SIZE/2 + horizontal_offset, piece.position[0] * SQUARE_SIZE + SQUARE_SIZE/2 + vertical_offset), PIECE_SIZE, 5)
        text_surface = symbol_font.render(piece.atom, True, (0,0,0))
        text_rect = text_surface.get_rect(center=(piece.position[1] * SQUARE_SIZE + SQUARE_SIZE/2 + horizontal_offset, piece.position[0] * SQUARE_SIZE + SQUARE_SIZE/2 + vertical_offset))
        screen.blit(text_surface, text_rect)

        # Desenha avElectrons:
        for electrons in range(piece.avElectrons):
            angle = (360 / piece.avElectrons) * electrons
            # Calcula a posição relativa do elétron de valência em relação ao átomo
            relative_x = int(pygame.math.Vector2(35, 0).rotate(angle).x)
            relative_y = int(pygame.math.Vector2(35, 0).rotate(angle).y)
            # Calcula a posição absoluta do elétron de valência em relação à tela
            x = piece.position[1] * SQUARE_SIZE + SQUARE_SIZE/2 + relative_x + horizontal_offset
            y = piece.position[0] * SQUARE_SIZE + SQUARE_SIZE/2 + relative_y + vertical_offset
            pygame.draw.circle(screen, white, (x , y), ELECTRON_SIZE)
            pygame.draw.circle(screen, (0,0,0), (x, y), ELECTRON_SIZE, 5)
            
# Menu to select the level
def drawMenuLevels(level_option, level_option_selected):
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
def drawMenuIA(menu_ia_options, menu_ia_selected):
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
def drawoptionsIA(algorithm_options, algorithm_selected):
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


def drawVictory(number_moves, time_elapsed):
    screen.fill("grey")
    font = pygame.font.SysFont("Arial", 50)

    # Render the victory text
    victory_text = font.render("Victory!", True, "black")
    victory_text_rect = victory_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 100))
    screen.blit(victory_text, victory_text_rect)

    # Render the number of moves
    moves_text = font.render(f"Number of moves: {number_moves}", True, "black")
    moves_text_rect = moves_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(moves_text, moves_text_rect)

    # Render the time elapsed
    time_text = font.render(f"Time elapsed: {time_elapsed:.3f} seconds", True, "black")
    time_text_rect = time_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 100))
    screen.blit(time_text, time_text_rect)

    pygame.display.flip()



def drawAbout():
    screen.fill("grey")

    # Draw the game name
    game_name_surface = game_name_font.render(game_name, True, "black")
    game_name_pos = game_name_surface.get_rect(midtop=(screen.get_width() // 2, screen.get_height() // 2 - 200))
    screen.blit(game_name_surface, game_name_pos)

    about_text = (
        "...is an elegantly designed puzzle game about chemistry. It's logical, minimalist, and beautiful."
    )
    bout = pygame.font.SysFont("Arial", 25).render(about_text, True, "black")
    out = bout.get_rect(midtop=(screen.get_width() // 2, screen.get_height() // 2 - 80))
    screen.blit(bout, out)

    command_text = (
    "Commands:"
    "  w - up      z - undo"
    "  s - down    r - restart"
    "  a - left"
    "  d - right"
    )

    ommand = pygame.font.SysFont("Arial", 25).render("Commands:", True, "black")
    mmand = bout.get_rect(midtop=(screen.get_width() // 2, screen.get_height() // 2 - 10))
    screen.blit(ommand, mmand)
    ommand = pygame.font.SysFont("Arial", 25).render("  w - up      z - undo", True, "black")
    mmand = bout.get_rect(midtop=(screen.get_width() // 2, screen.get_height() // 2 + 20))
    screen.blit(ommand, mmand)
    ommand = pygame.font.SysFont("Arial", 25).render("  s - down    q - restart", True, "black")
    mmand = bout.get_rect(midtop=(screen.get_width() // 2, screen.get_height() // 2 +50))
    screen.blit(ommand, mmand)
    ommand = pygame.font.SysFont("Arial", 25).render("  a - left", True, "black")
    mmand = bout.get_rect(midtop=(screen.get_width() // 2, screen.get_height() // 2 +80))
    screen.blit(ommand, mmand)
    ommand = pygame.font.SysFont("Arial", 25).render("  d - right", True, "black")
    mmand = bout.get_rect(midtop=(screen.get_width() // 2, screen.get_height() // 2 +110))
    screen.blit(ommand, mmand)
    


    


    pygame.display.flip()
    
