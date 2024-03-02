import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

#Game Name 
game_name = "SOKOBOND"

#Fonts
game_name_font = pygame.font.SysFont("Arial", 100)
menu_options_font = pygame.font.SysFont("Arial", 24)

# The options in the menu
menu_options = ["start game", "settings", "about", "quit"]
menu_option_selected = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN: #Options are controlled only by w and s 
            if event.key == pygame.K_w:
                menu_option_selected = (menu_option_selected - 1) % len(menu_options)
            elif event.key == pygame.K_s:
                menu_option_selected = (menu_option_selected + 1) % len(menu_options)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN: #Press Enter
                if menu_options[menu_option_selected] == "start game": #Start the game
                    pass
                if menu_options[menu_option_selected] == "settings": #Open settings
                    pass
                if menu_options[menu_option_selected] == "about": #Show settings
                    pass
                if menu_options[menu_option_selected] == "quit": #Quit the game
                    running = False

    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")
    
    #Draw the game name
    game_name_surface = game_name_font.render(game_name, True, "black")
    game_name_pos = game_name_surface.get_rect(midtop = (screen.get_width() // 2, screen.get_height() // 2 - 200))        
    screen.blit( game_name_surface,game_name_pos) 
    
    #Draw Menu
    for i, option in enumerate(menu_options):
        option = menu_options_font.render(option, True, "black")
        highlighted = option.get_rect(midtop = (screen.get_width() // 2, screen.get_height() // 2 + i* 50))
        if i == menu_option_selected:
            pygame.draw.rect(screen, "orange", highlighted.inflate(20,10)) # The rectangle shows in the option selected 
        screen.blit(option,highlighted) 

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()