#import modules
import pygame
from pygame.locals import *

#initialize pygame
pygame.init()

#set screen size
screen_width = 300
screen_height = 300

#create game window with a name
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TicTacToe')

#define variables
line_width = 6
markers = []

#creates the game board on the screen
def draw_grid():
    bg = (255, 255, 200)
    grid = (50, 50, 50)
    screen.fill(bg)
    for i in range (1, 3):
        pygame.draw.line(screen, grid, (0, i * 100), (screen_width, i * 100), line_width)
        pygame.draw.line(screen, grid, (i * 100, 0), (i * 100, screen_height), line_width)

for i in range(3):
    row = [0] * 3
    markers.append(row)

print(markers)

#create game loop with exit option
run = True
while run:

    draw_grid()

    #add event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update additions to the display
    pygame.display.update()

#quit pygame
pygame.quit()

