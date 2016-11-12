# Author: Sean Slater
# Version: 0.0.1
# Date: 2016-07-13

import sys, os, pygame, math, Globals, Hex, Point, Draw

cs = Globals.CELL_SIZE
mr = Globals.MAP_RADIUS


def main():
    pygame.init()
    m_width = int(((mr*cs*math.sqrt(3))+cs)*2)
    #m_width = int((math.sqrt(3) * Globals.CELL_SIZE) * Globals.MAP_RADIUS)
    m_height = int(((mr*cs)+((math.ceil(mr/2)+1)*cs))*2)
    #m_height = int(((math.ceil(Globals.MAP_RADIUS / 2) * Globals.CELL_SIZE * 2) + (math.floor(Globals.MAP_RADIUS / 2) * Globals.CELL_SIZE) * 2))
    size = m_width, m_height
    print size
    #size = 600, 600
    center = int(size[0]/2), int(size[1]/2)
    screen = pygame.display.set_mode(size)
    keys = pygame.key.get_pressed()
    grid = Hex.HexGrid(mr)


    color = 54,216,212

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()


        #screen.fill(color)
        Draw.draw(screen, grid, center)
        pygame.display.flip()

if __name__ == '__main__':
    main()


'''
pygame.init()
size = width, height = 1024, 576
speed = [1, 1]
color = 1, 1, 1
#screen = pygame.display.set_mode()
screen = pygame.display.set_mode(size)
ball = pygame.image.load('assets/ball.gif')
ballAction = ball.get_rect()
keys = pygame.key.get_pressed()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #if keys[pygame.K_ESCAPE]: sys.exit()

    ballAction = ballAction.move(speed)
    if ballAction.left < 0 or ballAction.right > width:
    #if keys[0] == pygame.K_DOWN:
        speed[0] = -speed[0]
    if ballAction.top < 0 or ballAction.bottom > height:
    #if keys[0] == pygame.K_UP:
        speed[1] = -speed[1]

    screen.fill(color)
    screen.blit(ball, ballAction)
    pygame.display.flip()
'''
