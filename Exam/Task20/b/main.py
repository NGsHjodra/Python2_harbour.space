import pygame


pygame.init()

w = 600
h = 600
bg_color = 'green'
drawing_color = 'blue'
radius = 30

window_size = pygame.math.Vector2(w, h)
pygame.display.set_mode(window_size)

done = False

x = w / 2
y = h / 2

while not done:

    pygame.display.get_surface().fill(bg_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: done = True

    surf = pygame.display.get_surface()
    pygame.draw.circle(surf, drawing_color, (x, y), radius)

    pygame.display.flip()

    radius += 0.1

pygame.quit()