### Data about the Hexes ###
import HashTable, Point, Globals

class HexCell:
    def __init__(self, q_pos, r_pos):
        self.point = Point.A_Point(q_pos, r_pos)

    def getKey(self):
        return str(self.point.x)+","+str(self.point.y)

    def getPos(self):
        return self.point

class HexGrid:
    def __init__(self, radius=Globals.MAP_RADIUS):
        self.radius = radius
        self.hexTable = HashTable.HashTable((6*((self.radius*(self.radius+1))/2))+1)
        self.generateGrid()

    def generateGrid(self):
        z = 0
        for x in range(-self.radius, self.radius+1):
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
