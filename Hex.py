### Data about the Hexes ###
import HashTable, Point, Globals, random

class HexCell:
    def __init__(self, q_pos, r_pos):
        self.point = Point.A_Point(q_pos, r_pos)
        self.tile = random.randint(0,3)
        self.value = random.randint(1,9)
        self.occupied = 0
        self.occImage = None
        self.resources = self.value

    def getKey(self):
        return str(self.point.x)+","+str(self.point.y)

    def getPos(self):
        return self.point

    def getTile(self):
        return self.tile

    def getValue(self):
        return self.value

    def setResources(self,val):
        self.resources -= val

    def resetResources(self):
        self.resources = self.value

    def getResources(self):
        return self.resources

    def isOccupied(self):
        return self.occupied

    def setOccupied(self, val):
        self.occupied = val

    def setOccImg(self, img):
        self.occImage = img

    def getOccImg(self):
        return self.occImage

class HexGrid:
    def __init__(self, radius=Globals.MAP_RADIUS):
        self.radius = radius
        self.hexTable = HashTable.HashTable((6*((self.radius*(self.radius+1))/2))+1)
        self.generateGrid()

    def generateGrid(self):
        z = 0
        for x in range(-self.radius, 1):
            for y in range(z, self.radius+1):
                h = HexCell(x,y)
                p = str(x)+","+str(y)
                self.hexTable.set(p,h)
            z -= 1
        z = self.radius
        for x in range(1, self.radius+1):
            for y in range(-self.radius, z):
                h = HexCell(x,y)
                p = str(x)+","+str(y)
                self.hexTable.set(p,h)
            z -= 1

    def setHex(self, h):
        self.hexTable.set(h.getPos(),h)


    def getHex(self, p):
        return self.hexTable.get(p)

    def getTable(self):
        return self.hexTable
