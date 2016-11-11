import occ_grid
import entities
import pygame


# define cell size
CELL_SIZE = 10

# define some colors to be used for drawing
GREEN    = (20, 225, 0)
YELLOW   = (240, 245, 13)
PURPLE   = (240, 5, 213)
BLUE     = (5, 25, 240)
RED      = (250, 25, 5)

# load all of the images

floor = pygame.image.load('Floor.bmp')
bank = pygame.image.load('Bank.bmp')
robber = pygame.image.load('Robber.bmp')
money = pygame.image.load('Money.bmp')
coin = pygame.image.load('Coins.bmp')
cop = pygame.image.load('Cop.bmp')
dust = pygame.image.load('Dust.bmp')

# determine sprite image based on occupancy value

def determineSprite(occupancy_value):
   if occupancy_value == occ_grid.EMPTY:
      return floor
   elif occupancy_value == occ_grid.GATHERER:
      return robber
   elif occupancy_value == occ_grid.GENERATOR:
      return bank
   elif occupancy_value == occ_grid.RESOURCE:
      return money
   elif occupancy_value == occ_grid.TRAIL:
      return dust
   elif occupancy_value == occ_grid.RESOURCE_SPAWN:
      return coin
   elif occupancy_value == occ_grid.CHASER:
      return cop
   else:
      return RED


# determine cell color based on occupancy value
def determineColor(occupancy_value):
   if occupancy_value == occ_grid.EMPTY:
      return BLUE
   elif occupancy_value == occ_grid.GATHERER:
      return YELLOW
   elif occupancy_value == occ_grid.GENERATOR:
      return PURPLE
   elif occupancy_value == occ_grid.RESOURCE:
      return GREEN
   else:
      return RED


# draw the 2D grid
def draw_sprites(screen, grid, cell_size):
   for y in range(0, grid.height):
      for x in range(0, grid.width):
         sprite = determineSprite(occ_grid.get_cell(grid, entities.Point(x, y)))
         new_sprite = pygame.transform.scale(sprite, (CELL_SIZE, CELL_SIZE))
         screen.blit(new_sprite, (x * CELL_SIZE, y * CELL_SIZE))
