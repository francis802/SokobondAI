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


def display(screen, game, game_name, symbol_font,game_name_font, menu_options, menu_options_font, menu_option_selected, game_started):
    screen.fill("grey")
    
    if not game_started:
        drawMenu(screen, game_name, game_name_font, menu_options, menu_options_font, menu_option_selected)
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

        for piece in game.pieces:
            # Draw connections:
                for connection in piece.connections:
                    pygame.draw.line(screen, (0,0,0), (piece.position[1] * 100 + 50, piece.position[0] * 100 + 50), (connection.position[1] * 100 + 50, connection.position[0] * 100 + 50), 5)    

            # Draw the piece:
                pygame.draw.circle(screen, COLORS[piece.atom], (piece.position[1] * 100 + 50, piece.position[0] * 100 + 50), 40)
                pygame.draw.circle(screen, (0,0,0), (piece.position[1] * 100 + 50, piece.position[0] * 100 + 50), 40, 5)
                text_surface = symbol_font.render(piece.atom, True, (0,0,0))
                text_rect = text_surface.get_rect(center=(piece.position[1] * 100 + 50, piece.position[0] * 100 + 50))
                screen.blit(text_surface, text_rect)

            # Draw avElectrons:
                for atoms in range(piece.avElectrons):
                    angle = (360 / piece.avElectrons) * atoms
                    # Calcular a posição relativa do elétron de valência em relação ao átomo
                    relative_x = int(30 * pygame.math.Vector2().rotate(angle).x)
                    relative_y = int(30 * pygame.math.Vector2().rotate(angle).y)
                    # Calcular a posição absoluta do elétron de valência em relação à tela
                    x = piece.position[1] * 100 + 76 + relative_x
                    y = piece.position[0] * 100 + 76 + relative_y
                    pygame.draw.circle(screen, white, (x , y), 10)
                    pygame.draw.circle(screen, (0,0,0), (x, y), 10, 5)
            
             
         


        

           
