import pygame

pygame.init()

# Setting up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("SpaceX GAME")

# Loading background image and font
background = pygame.image.load("background.jpg")
font = pygame.font.Font(None, 36)

# Welcome Screen
welcome_text = font.render("Welcome to Adventure of SpaceX!!!", True, (255, 255, 255))
press_enter_text = font.render("Press ENTER to start playing", True, (255, 255, 255))
while True:
    screen.blit(background, (0, 0))
    screen.blit(welcome_text, (200 ,200))
    screen.blit(press_enter_text, (233, 280))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Starting the game
                exec(open("pygame_basic.py").read())
                # Game has ended, showing play again and exit options
                pygame.mixer.music.stop()  # Stop the background music
                play_again_text = font.render("Press ENTER to play again", True, (255, 255, 255))
                exit_text = font.render("Press ESC to exit", True, (255, 255, 255))
                while True:
                    screen.blit(background, (0, 0))
                    screen.blit(play_again_text, (250, 200))
                    screen.blit(exit_text, (250, 300))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                exec(open("pygame_basic.py").read())
                                # Game has ended again, showing play again and exit options
                                play_again_text = font.render("Press ENTER to play again", True, (255, 255, 255))
                                exit_text = font.render("Press ESC to exit", True, (255, 255, 255))
                            elif event.key == pygame.K_ESCAPE:
                                pygame.quit()
                                quit()
                    pygame.display.update()

    pygame.display.update()
