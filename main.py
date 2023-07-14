import pygame
import logic

# pygame setup
pygame.init()
p1 = logic.Mouse_position()
clock = pygame.time.Clock()
running = True
dt = 0
pygame.display.set_caption('Tic Tac Toe')

player_pos = pygame.Vector2(p1.screen.get_width() / 2, p1.screen.get_height() / 2)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    p1.screen.fill("cyan")
    p1.draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            p1.position = (pygame.mouse.get_pos())
            p1.squares()                                #which square was clicked
            #if p1.valid_move:
                #p1.check_if_win()
                #p1.computers_move()
                #p1.check_if_win()

    p1.drawXO()
    if p1.valid_move == 1:
        p1.check_if_win()
        p1.computers_move()
        p1.check_if_win()
        p1.valid_move = 0


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

