import entities
import occ_grid
import movement
import create
import pygame

def controls(robbers, moneys):
   keys = pygame.key.get_pressed()
   if keys[pygame.K_1]:
      robbers.far = False
      robbers.wheretogo = movement.nearest(robbers, moneys)
      print("one")
   if keys[pygame.K_2]:
      robbers.far = True
      robbers.wheretogo = movement.farthest(robbers, moneys)
      print("two")
   if keys[pygame.K_0]:
      print("zero")
      
def start(Robbers):
   keys = pygame.key.get_pressed()
   if keys[pygame.K_SPACE]:
      Robbers.moving = True
      print("space")
      return True
      
def reset(grid, robbers, Bank, moneys):
   key = pygame.key.get_pressed()
   if key[pygame.K_0]:
      for y in range(0,59):
         for z in range (0,59):
            occ_grid.set_cell(grid, entities.Point(y,z), occ_grid.EMPTY)   
      
      robbers.position.x = create.robpt_x
      robbers.position.y = create.robpt_y
      robbers.moving = False
      occ_grid.set_cell(grid, entities.Point(create.robpt_x, create.robpt_y), occ_grid.GATHERER)
      occ_grid.set_cell(grid, Bank.position, occ_grid.GENERATOR)
      for x in range(0, len(moneys)):
         occ_grid.set_cell(grid, moneys[x].position, occ_grid.RESOURCE)
      robbers.move = False
