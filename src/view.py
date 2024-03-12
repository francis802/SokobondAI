import pygame


#Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
grey = (128,128,128)

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


def display(screen, game, game_name, game_name_font, menu_options, menu_options_font, menu_option_selected, game_started):
    screen.fill("grey")
    
    if not game_started:
        drawMenu(screen, game_name, game_name_font, menu_options, menu_options_font, menu_option_selected)
    else:
        drawGame(screen, game) 
   
   
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


def drawGame(screen, game):
        for wall in game.walls:
            pygame.draw.rect(screen, grey, (wall[1] * 100, wall[0] * 100, 100, 100))

        for piece in game.pieces:
            pygame.draw.circle(screen, COLORS[piece.atom], (piece.position[1] * 100 + 50, piece.position[0] * 100 + 50), 40)
        

           
