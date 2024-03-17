import pygame
from pygame.locals import *
import random
import sys

board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

players = ['X', 'O']
currentPlayer = random.randint(0, len(players) - 1)
available = [(i, j) for j in range(3) for i in range(3)]
lh = 3


def equals3(a, b, c):
    return a == b and b == c and a != ''


def nextTurn():
    global currentPlayer
    if not available:
        return
    spot = random.choice(available)
    available.remove(spot)
    i, j = spot
    board[i][j] = players[currentPlayer]
    currentPlayer = (currentPlayer + 1) % len(players)


def checkWinner():
    winner = None

    for i in range(3):
        if equals3(board[i][0], board[i][1], board[i][2]):
            winner = board[i][0]
    for i in range(3):
        if equals3(board[0][i], board[1][i], board[2][i]):
            winner = board[0][i]
    if equals3(board[0][0], board[1][1], board[2][2]):
        winner = board[0][0]
    if equals3(board[2][0], board[1][1], board[0][2]):
        winner = board[2][0]

    return winner


def draw():
    w = width / 3
    h = height / 3

    pygame.draw.line(screen, (0, 0, 0), (w, 0), (w, height), lh)
    pygame.draw.line(screen, (0, 0, 0), (w * 2, 0), (w * 2, height), lh)
    pygame.draw.line(screen, (0, 0, 0), (0, h), (width, h), lh)
    pygame.draw.line(screen, (0, 0, 0), (0, h * 2), (width, h * 2), lh)

    for j in range(3):
        for i in range(3):
            x = w * i + w / 2
            y = h * j + h / 2

            spot = board[i][j]
            if spot == players[0]:
                xr = w / 4
                pygame.draw.line(screen, (0, 0, 0), (x - xr, y - xr), (x + xr, y + xr), lh)
                pygame.draw.line(screen, (0, 0, 0), (x + xr, y - xr), (x - xr, y + xr), lh)
            elif spot == players[1]:
                pygame.draw.circle(screen, (0, 0, 0), (int(x), int(y)), int(w / 3), lh)
    result = checkWinner()
    if result is not None:
        print(result)
        pygame.image.save(screen, '.github/images/image.jpg')
    nextTurn()


def eventHandler():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


pygame.init()
fps = 1
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

while True:
    screen.fill((255, 255, 255))

    eventHandler()
    draw()
    pygame.display.flip()
    clock.tick(fps)
