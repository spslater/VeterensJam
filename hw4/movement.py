import entities
import occ_grid
import math


def distance(rob, mon):
   return math.sqrt((rob.position.x-mon.position.x)**2+(rob.position.y-mon.position.y)**2)

def farthest(robber, moneys):
   far = robber
   for entitie in moneys:
      if distance(robber, entitie) > distance(robber, far):
         far = entitie
   return far

def nearest(robber, moneys):
   near = entities.Money("Dollar", entities.Point(100000000,100000000))
   for entitie in moneys:
      if distance(robber, entitie) < distance(robber, near):
         near = entitie
   return near

def makeRobberGo(robbers, Money):
   if robbers.moving:
      if robbers.far:
         goto = robbers.wheretogo
         determineNewGathererPosition(robbers, goto)
      else:
         goto = robbers.wheretogo
         determineNewGathererPosition(robbers, goto)

def determineNewGathererPosition(Robbers, Money):
   if Robbers.position.x < Money.position.x:
      Robbers.position.x = Robbers.position.x + 1
   elif Robbers.position.x > Money.position.x:
      Robbers.position.x = Robbers.position.x - 1
   else:
      if Robbers.position.y < Money.position.y:
         Robbers.position.y = Robbers.position.y + 1
      elif Robbers.position.y > Money.position.y:
         Robbers.position.y = Robbers.position.y - 1
         
def robber_trail(grid):
   for x in range(0, 59):
      for y in range(0, 59):
         if occ_grid.get_cell(grid, entities.Point(x, y)) == occ_grid.GATHERER:
            occ_grid.set_cell(grid, entities.Point(x, y), occ_grid.TRAIL)