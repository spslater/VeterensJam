# base 2D grid world that draws a different color circle for each element type 
import math
import random
import entities
import occ_grid
import sol
import controller
import images
import create
import sys, pygame
from pygame.locals import *

# function to start up the main drawing
def main():
   pygame.init()
   screen = pygame.display.set_mode((60 * images.CELL_SIZE, 60 * images.CELL_SIZE))
   event = pygame.event.poll()
   keys = pygame.key.get_pressed()
   grid = occ_grid.Grid(60, 60, occ_grid.EMPTY)
   Robbers, Bank, moneys = create.createEntities(grid)
   sol.placeEntities(grid, Robbers, Bank, moneys)


   while 1:
      for event in pygame.event.get():
         if event.type == QUIT: sys.exit()

      controller.reset(grid, Robbers, Bank, moneys)
      create.resourceEffect(grid, event, moneys)

      images.draw_sprites(screen, grid, images.CELL_SIZE)
      pygame.display.flip()
      create.resourceEffect(grid, event, Bank)
      sol.updateEntities(grid, Robbers, Bank, moneys)


if __name__ == '__main__':
   main()
