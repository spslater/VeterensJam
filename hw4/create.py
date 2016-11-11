import entities
import occ_grid
import random
import pygame

robpt_x = random.randint(0,59)
robpt_y = random.randint(0,59)

def createEntities(grid):
   Robbers = entities.Robbers("Joe", 5, 0, entities.Point(robpt_x, robpt_y))
   Bank = entities.Bank("Bank", 5, entities.Point(random.randint(2, 57), (random.randint(2, 57))))
   numbers = moneyLocation(Bank)
   moneys = []
   for z in numbers:
      if z != [0, 0]:
         moneys.append(entities.Money("Dollar", entities.Point(int(z[0]), int(z[1]))))
   #print (moneys)
   return (Robbers, Bank, moneys)

def px_to_grid(x, y):
   x = int(x/10)
   y = int(y/10)
   return entities.Point(x, y)

def resourceEffect(grid, event, dollar):
   if event.type == pygame.MOUSEBUTTONDOWN:
      x_pos, y_pos = event.pos
      grid_pos = px_to_grid(x_pos, y_pos)
      cell_info = occ_grid.get_cell(grid, grid_pos)
      if cell_info == 3:
         spawnCoins(grid, grid_pos, dollar)
      print(cell_info, x_pos, y_pos)

def spawnCoins(grid, grid_pos, moneys):
   cell_info = occ_grid.get_cell(grid, grid_pos)
   for q in range(0, 8): 
      if q == 1 and cell_info == 0:
         pos = entities.Point(moneys.position.x - 1, moneys.position.y - 1)
         return occ_grid.set_cell(grid, pos, occ_grid.RESOURCE_SPAWN)
      if q == 2 and cell_info == 0 :
         pos = entities.Point(moneys.position.x, moneys.position.y - 1)
         return occ_grid.set_cell(grid, pos, occ_grid.RESOURCE_SPAWN)
      if q == 3 and cell_info == 0:
         pos = entities.Point(moneys.position.x + 1, moneys.position.y - 1)
         return occ_grid.set_cell(grid, pos, occ_grid.RESOURCE_SPAWN)
      if q == 4 and cell_info == 0:
         pos = entities.Point(moneys.position.x - 1, moneys.position.y)
         return occ_grid.set_cell(grid, pos, occ_grid.RESOURCE_SPAWN)
      if q == 5 and cell_info == 0:
         pos = entities.Point(moneys.position.x + 1, moneys.position.y)
         return occ_grid.set_cell(grid, pos, occ_grid.RESOURCE_SPAWN)
      if q == 6 and cell_info == 0:
         pos = entities.Point(moneys.position.x - 1, moneys.position.y + 1)
         return occ_grid.set_cell(grid, pos, occ_grid.RESOURCE_SPAWN)
      if q == 7 and cell_info == 0:
         pos = entities.Point(moneys.position.x, moneys.position.y - 1)
         occ_grid.set_cell(grid, pos, occ_grid.RESOURCE_SPAWN)
      if q == 8 and cell_info == 0:
         pos = entities.Point(moneys.position.x + 1, moneys.position.y + 1)
         return occ_grid.set_cell(grid, pos, occ_grid.RESOURCE_SPAWN)

def moneyLocation(bank):
   POSITIONS = []
   for mon in range(0, random.randint(3,10)):
      mon = bank.position.x + random.randint(-2,2)
      bon = bank.position.y + random.randint(-2,2)
      POSITIONS.append([mon, bon])
   #print(POSITIONS)
   return POSITIONS
