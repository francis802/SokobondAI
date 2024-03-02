import pygame
from levels import levels

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

#Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
grey = (128,128,128)

# Board colors
COLORS = {
    'r': red,
    'g': green,
    'b': blue,
    'y': yellow,
    'g': grey,
    None: white
}

# Player position
player_pos = None



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                menu_option_selected = (menu_option_selected - 1) % len(menu_options)
            elif event.key == pygame.K_s:
                menu_option_selected = (menu_option_selected + 1) % len(menu_options)
            elif event.key == pygame.K_RETURN:  # Press Enter
                if menu_options[menu_option_selected] == "start game":
                    game_started = True
                elif menu_options[menu_option_selected] == "quit":
                    running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")

    if not game_started:
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
        else:
        # only for test the design of the levels (appears on the same screen as the main menu)
         for row_index, row in enumerate(levels[4]):  
            for col_index, cell in enumerate(row):
                if cell:
                    color = COLORS[cell[:3]]
                    # Draw circle for red and blue, rectangle for others
                    if color in (red, blue):
                        pygame.draw.circle(screen, color, (col_index * 100 + 50, row_index * 100 + 50), 40)
                    else:
                        pygame.draw.rect(screen, color, (col_index * 100, row_index * 100, 100, 100))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
