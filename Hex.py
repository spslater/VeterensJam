### Data about the Hexes ###
import HashTable, Point

class HexCell:
    def __init__(self, q_pos, r_pos):
        self.point = A_Point(q_pos, r_pos)

    def getPos(self):
        return str(self.q)+","+str(self.r)


class HexGrid:
    def __init__(self, radius=MAP_RADIUS):
        self.radius = radius
        self.hexTable = HashTable.HashTable((6*((self.radius*(self.radius+1))/2))+1)

    def generateGrid(self):
        z = 0
        for x in range(-self.radius, self.radius+1):
            for y in range(z, self.radius+1):
                h = HexCell(x,y)
                p = str(x)+","+str(y)
                self.hexTable.set(p,h)
                print p
            z -= 1
        z = self.radius
        for x in range(1, self.radius+1):
            for y in range(-self.radius, z):
                h = HexCell(x,y)
                p = str(x)+","+str(y)
                self.hexTable.set(p,h)
                print p
            z -= 1

    def setHex(h):
        hexTable.set(h.getPos(),h)


    def getHex(p):
        return hexTable.get(p)
