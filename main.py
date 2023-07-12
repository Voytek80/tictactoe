import pygame
import logic

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
p1 = logic.Mouse_position()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    screen.fill("purple")
    pygame.draw.line(screen, "black", (200, 0), (200, 600), 10)
    pygame.draw.line(screen, "black", (400, 0), (400, 600), 10)
    pygame.draw.line(screen, "black", (0, 200), (600, 200), 10)
    pygame.draw.line(screen, "black", (0, 400), (600, 400), 10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            p1.position = (pygame.mouse.get_pos())
            p1.squares()
            p1.computers_move()






    for i, j in enumerate(p1.square):
        if j == 1:
            a1, a2 = p1.draw_x_coordinates(i)
            b1, b2 = a1
            c1, c2 = a2
            pygame.draw.line(screen, "black", b1, b2, 10)
            pygame.draw.line(screen, "black", c1, c2, 10)











    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()