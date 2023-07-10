import pygame
import mouse_position

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
p1 = mouse_position.Mouse_position()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            p1.position = (pygame.mouse.get_pos())
            print(p1.squares(), p1.position)
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    pygame.draw.line(screen, "black", (200, 0), (200, 600), 10)
    pygame.draw.line(screen, "black", (400, 0), (400, 600), 10)
    pygame.draw.line(screen, "black", (0, 200), (600, 200), 10)
    pygame.draw.line(screen, "black", (0, 400), (600, 400), 10)






    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()