import time

import pygame
import socket

import logging

logging.basicConfig(
    filename='game.log',
    encoding='utf-8',
    level=logging.DEBUG,
    format='%(asctime)s\t%(levelname)s\t%(message)s'
)
logging.info('Program started.')

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 8080  # The port used by the server

class Ball:
    def __init__(self, x, y, color):
        self.color = color
        self.x = x
        self.y = y


pygame.init()

w = 600
h = 600
bg_color = 'green'
drawing_color = 'blue'
radius = 30

window_size = pygame.math.Vector2(w, h)
pygame.display.set_mode(window_size)

logging.info(f'Window created {w}x{h}')

done = False

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

my = Ball(w/2, h/2, "red")

other = Ball(w/2, h/2, "blue")

food = Ball(w/2, h/2, "yellow")

counter = 0
start = time.time()

while not done:

    pygame.display.get_surface().fill(bg_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        my.x -= 0.1
    if keys[pygame.K_RIGHT]:
        my.x += 0.1
    if keys[pygame.K_UP]:
        my.y -= 0.1
    if keys[pygame.K_DOWN]:
        my.y += 0.1

    s.sendall(bytearray(f"{my.x};{my.y}", 'utf-8'))

    data = s.recv(200)
    decoded_data = data.decode('utf-8')
    left, right = decoded_data.split('>')
    other.x, other.y = left.split(';')
    food.x, food.y = right.split(';')
    other.x = float(other.x)
    other.y = float(other.y)
    food.x = float(food.x)
    food.y = float(food.y)


    surf = pygame.display.get_surface()
    pygame.draw.circle(surf, my.color, (my.x, my.y), radius)
    pygame.draw.circle(surf, other.color, (other.x, other.y), radius)
    pygame.draw.circle(surf, food.color, (food.x, food.y), radius/2)

    pygame.display.flip()
    
    counter += 1
    if counter % 500 == 0:
        time_passed = time.time() - start
        logging.debug(f'Frames: {counter}, time: {time_passed}, avg. fps: {counter / time_passed}')
    
    

#    x += 0.1

pygame.quit()