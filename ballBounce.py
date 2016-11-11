# Author: Sean Slater
# Version: 1.0.1
# Date: 2016-07-13

import sys
import pygame

pygame.init()
size = width, height = 800, 500
speed = [2, 1]
color = 1, 1, 1
screen = pygame.display.set_mode(size)
ball = pygame.image.load('assets/ball.gif')
ballAction = ball.get_rect()
while True:
      for event in pygame.event.get():
          if event.type == pygame.QUIT: sys.exit()

      ballAction = ballAction.move(speed)
      if ballAction.left < 0 or ballAction.right > width:
        speed[0] = -speed[0]
      if ballAction.top < 0 or ballAction.bottom > height:
          speed[1] = -speed[1]

      screen.fill(color)
      screen.blit(ball, ballAction)
      pygame.display.flip()
