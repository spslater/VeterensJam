import occ_grid
import controller
import movement

def placeEntities(grid, Robbers, Bank, moneys):
   occ_grid.set_cell(grid, Robbers.position, occ_grid.GATHERER)
   occ_grid.set_cell(grid, Bank.position, occ_grid.GENERATOR)
   for x in range(0, len(moneys)):
      occ_grid.set_cell(grid, moneys[x].position, occ_grid.RESOURCE)
  
def isValidPosition(Robbers):
   if 0 <= Robbers.position.x < 60 and 0 <= Robbers.position.y < 60:
      return True
   else:
      return False

def updateEntities(grid, robbers, Bank, Money):
   controller.controls(robbers, Money)
   movement.robber_trail(grid)
   controller.start(robbers)
   movement.makeRobberGo(robbers, Money)
   if isValidPosition(robbers) == True:
      occ_grid.set_cell(grid, robbers.position, occ_grid.GATHERER)