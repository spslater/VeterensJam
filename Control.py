import pygame, sys

P1UL = pygame.K_w
P1UR = pygame.K_r
P1LL = pygame.K_s
P1RR = pygame.K_f
P1DL = pygame.K_x
P1DR = pygame.K_v

P2UL = pygame.K_u
P2UR = pygame.K_o
P2LL = pygame.K_j
P2RR = pygame.K_l
P2DL = pygame.K_m
P2DR = pygame.K_PERIOD


def keyProcess(key, players, grid):
    if key == pygame.K_LSHIFT:
        players[1].playTurn(grid)
        print "P1 Submits Move"
    if key == pygame.K_RSHIFT:
        players[2].playTurn(grid)
        print "P2 Submits Move"
    if key == P1UL:
        players[1].setPos(0,-1)
        print "P1 moves Up-Left"
    elif key == P1UR:
        players[1].setPos(1,-1)
        print "P1 moves Up-Right"
    elif key == P1LL:
        players[1].setPos(-1,0)
        print "P1 moves Left"
    elif key == P1RR:
        players[1].setPos(1,0)
        print "P1 moves Right"
    elif key == P1DL:
        players[1].setPos(-1,1)
        print "P1 moves Down-Left"
    elif key == P1DR:
        players[1].setPos(0,1)
        print "P1 moves Down-Right"
    elif key == P2UL:
        players[2].setPos(0,-1)
        print "P2 moves Up-Left"
    elif key == P2UR:
        players[2].setPos(1,-1)
        print "P2 moves Up-Right"
    elif key == P2LL:
        players[2].setPos(-1,0)
        print "P2 moves Left"
    elif key == P2RR:
        players[2].setPos(1,0)
        print "P2 moves Right"
    elif key == P2DL:
        players[2].setPos(-1,1)
        print "P2 moves Down-Left"
    elif key == P2DR:
        players[2].setPos(0,1)
        print "P2 moves Down-Right"
    elif key == pygame.K_ESCAPE or key == pygame.K_SPACE:
        sys.exit()
