import Globals, math

class P_Point:
    def __init__(sefl,x,y):
        self.x = x
        self.y = y

    def getPos(self):
        return self.x+","self.y


    def toAxial(self):
        x = self.x * (2/3) / CELL_SIZE
        y = (-self.x / 3 + math.sqrt(3) / 3 * self.y) / CELL_SIZE
        return hexRound(A_Point(int(x),int(y))

class A_Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getPos(self):
        return self.x+","self.y


    def toCube():
        x = self.x
        z = self.y
        y = -x-z
        return C_Point(x,y,z)

    def toOffset():
        return toCube().toOffset()

    def toPixel():
        x = CELL_SIZE * (3/2) * self.x
        y = CELL_SIZE * math.sqrt(3) * (self.y + self.x/2)
        return P_Point(int(x),int(y))


class C_Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z


    def getPos(self):
        return self.x+","self.y+","+self.z

    def toAxial():
        x = self.x
        y = self.z
        return A_Point(x,y)

    def toOffset():
        q = self.x + (self.z - (self.z&1)) /2
        r = self.z
        return O_Point(int(q),int(r))

class O_Point:  # Odd-row
    def __init__(self,q,r):
        self.q = q
        self.r = r

    def getPos(self):
        return self.q+","self.r

    def toCube():
        x = self.q - (self.r - (self.r&1)) / 2
        z = self.r
        y = -x-z
        return C_Point(int(x),int(y),int(z))

    def toAxial():
        return toCube().toAxial()
