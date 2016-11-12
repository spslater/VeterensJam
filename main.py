# Author: Sean Slater
# Version: 0.0.1
# Date: 2016-07-13

import sys, os, pygame, math, Globals


def main():
    pygame.init()
    m_width = int(((math.ceil(MAP_RADIUS / 2) * CELL_SIZE * 2) + (math.floor(MAP_RADIUS / 2) * CELL_SIZE) * 2))
    m_height = int((math.sqrt(3) * CELL_SIZE) * MAP_RADIUS)
    size = m_width, m_height
    center = int(m_width/2), int(m_height/2)
    screen = pygame.display.set_mode(size)
    keys = pygame.key.get_pressed()

    color = 54,216,212

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()


        screen.fill(color)
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
