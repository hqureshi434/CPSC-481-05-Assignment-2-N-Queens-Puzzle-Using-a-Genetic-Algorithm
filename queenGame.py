"""
Henry Torres
Ricky Martinez
Hammad Qureshi
"""
import pygame
import sys
from pygame.locals import *
from search import *

# initialize the pygame
pygame.init()
pygame.font.init()

# Initialize the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

# initialize the screen ((width, height))
screen = pygame.display.set_mode((1000, 800))
screen.fill((255, 255, 255))

# Caption and Icon
pygame.display.set_caption("The N-Queens Problem")
icon = pygame.image.load('queen.png')
pygame.display.set_icon(icon)

# Queen Image
queenImg = pygame.image.load('queen.png')
cancelImg = pygame.image.load('cancel.png')
evil_queenImg = pygame.image.load('evil_queen.png')


def chess(state):
    square = 90
    space = 40

    colors = [WHITE, BLACK]

    state_length = len(state)

    # initialize the screen display
    screen = pygame.display.set_mode((square * state_length + space * 2, square * state_length + space * 2))
    screen.fill((128, 128, 128))
    
    # print the states on top of chess board
    myFont = pygame.font.SysFont("Arial", 25)
    textSurface = myFont.render("The best individual " + str(state), False, (0, 0, 0))
    screen.blit(textSurface,((100,0)))

    # draw the squares of the chessbaord, either black or white
    for i in range(state_length) :
        for j in range(state_length):
                pygame.draw.rect(screen, colors[(i+j)%2], (space + square * i, space + square * j, square, square))

    # find the center of the square
    newPos = (space + square)/2

    # print the image of the queen on the correct squares
    for col, row in enumerate(state):
        screen.blit(queenImg, [newPos + square * col, newPos + square * row])

    # run the display
    running = True
    while running:
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                sys.exit()

newText = pygame.font.SysFont('Arial', 23)
user_input = ""

input_message = newText.render("Please enter a number of queens: ", True, BLACK)
screen.blit(input_message, (0,10))
screen.blit(evil_queenImg, (-250, -45))

def error(N):
    screen = pygame.display.set_mode((800, 600))
    screen.fill((255, 255, 255))

    badNum = newText.render("There are no solutions for " + str(N) + " queens problem!", True, BLACK)
    screen.blit(badNum, (0,10))
    screen.blit(cancelImg, (200, 200))

    running = True
    while running:
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                sys.exit()


running = True
while running:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[:len(user_input) - 1]
            
            elif event.key == pygame.K_RETURN:
                N = int(user_input)

                if N == 1:
                    chess([0])
                elif N < 4:
                    error(N)
                else:
                    state = genetic_search(NQueensProblem(N), n = 20, pmut = 0.9)
                    chess(state)
                
            elif len(user_input) < 2 and event.unicode.isnumeric():
                user_input += event.unicode
        
        pygame.draw.rect(screen, WHITE, (350,10,20,20))
        input_display = newText.render(user_input, True, BLACK)
        screen.blit(input_display, (350, 10))

