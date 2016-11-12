import Globals, math

cs = Globals.CELL_SIZE


class P_Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getKey(self):
        return str(self.x)+","+str(self.y)

    def getPos(self):
        return (self.x,self.y)

    def toAxial(self):
        x = (self.x * math.sqrt(3)/3 - self.y/3.0) / cs
        y = self.y * (2.0/3.0) * cs
        return A_Point(int(x),int(y)) # hexRound(A_Point(int(x),int(y)))

class A_Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getKey(self):
        return str(self.x)+","+str(self.y)

    def getPos(self):
        return (self.x,self.y)

    def toPixel(self):
        x = (cs * math.sqrt(3.0) * (self.x + self.y/2.0))
        y = (cs * (3.0/2.0) * self.y)
        return P_Point(int(x),int(y))
