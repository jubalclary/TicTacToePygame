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
winner = 0
game_over = False
again_rect = Rect(screen_width // 2 - 80, screen_height // 2, 160, 50)

green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

font = pygame.font.SysFont(None, 40)

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

#checks to see if the game has ended with a winner
def check_winner():
    global winner
    global game_over
    y_pos = 0
    for x in markers:
        #check columns
        if sum(x) == 3:
            winner = 1
            game_over = True
        if sum(x) == -3:
            winner = 2
            game_over = True 
        #check rows
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
            winner = 1
            game_over = True
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
            winner = 2
            game_over = True
        y_pos += 1
    #check diagonals
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
        winner = 1
        game_over = True
    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][0] + markers[1][1] + markers[0][2] == -3:
        winner = 2
        game_over = True

#Displays the winner and an option to play again
def draw_winner(winner):
    win_text = 'Player ' + str(winner) + ' wins!'
    win_img = font.render(win_text, True, blue)
    pygame.draw.rect(screen, green, (screen_width // 2 - 100, screen_height // 2 - 60, 200, 50))
    screen.blit(win_img, (screen_width // 2 - 95, screen_height // 2 - 50))

    again_text = 'Play Again'
    again_img = font.render(again_text, True, blue)
    pygame.draw.rect(screen, green, again_rect)
    screen.blit(again_img, (screen_width // 2 - 73, screen_height // 2 + 10))

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
        if game_over == 0:
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
                    check_winner()

    #Display the winner
    if game_over == True:
        draw_winner(winner)
        #check for user click on Play Again
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                #reset variables
                markers = []
                pos = []
                player = 1
                winner = 0
                game_over = False
                for i in range(3):
                    row = [0] * 3
                    markers.append(row)

    #update additions to the display
    pygame.display.update()

#quit pygame
pygame.quit()

