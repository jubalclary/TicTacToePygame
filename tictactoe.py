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
clicked = False
pos = []
player = 1

green = (0, 255, 0)
red = (255, 0, 0)

#creates the game board on the screen
def draw_grid():
    bg = (255, 255, 200)
    grid = (50, 50, 50)
    screen.fill(bg)
    for i in range (1, 3):
        pygame.draw.line(screen, grid, (0, i * 100), (screen_width, i * 100), line_width)
        pygame.draw.line(screen, grid, (i * 100, 0), (i * 100, screen_height), line_width)

#set up markers for the 3 rows and 3 columns of the game board
for i in range(3):
    row = [0] * 3
    markers.append(row)

#draws a marker in the clicked cell depending on the player
def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 85), (x_pos * 100 + 85, y_pos * 100 + 15), line_width)
            if y == -1:
                pygame.draw.circle(screen, red, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
            y_pos += 1
        x_pos += 1


#create game loop with exit option
run = True
while run:

    draw_grid()
    draw_markers()

    #add event handlers
    for event in pygame.event.get():

        #quit game
        if event.type == pygame.QUIT:
            run = False

        #get position of mouse when clicked and determines player
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            cell_x = pos[0]
            cell_y = pos[1]
            if markers[cell_x // 100][cell_y // 100] == 0:
                markers[cell_x // 100][cell_y // 100] = player
                player *= -1


    #update additions to the display
    pygame.display.update()

#quit pygame
pygame.quit()

