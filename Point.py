import Globals, math

cs = Globals.CELL_SIZE


class P_Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getPos(self):
        return (self.x,self.y)

    def toAxial(self):
        x = (self.x * math.sqrt(3)/3 - self.y/3) / cs
        y = self.y * (2/3) * cs
        return A_Point(int(x),int(y)) # hexRound(A_Point(int(x),int(y)))

class A_Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getKey(self):
        return self.x+","+self.y

    def getPos(self):
        return (self.x,self.y)

        '''
    def toCube(self):
        x = self.x
        z = self.y
        y = -x-z
        return C_Point(x,y,z)

    def toOffset(self):
        return toCube().toOffset()
'''
    def toPixel(self):
        x = (cs * math.sqrt(3) * (self.x + self.y/2))
        y = (cs * (3/2) * self.y)
        return P_Point(int(x),int(y))


        '''
class C_Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z


    def getKey(self):
        return self.x+","+self.y+","+self.z

    def toAxial(self):
        x = self.x
        y = self.z
        return A_Point(x,y)

    def toOffset(self):
        q = self.x + (self.z - (self.z&1)) /2
        r = self.z
        return O_Point(int(q),int(r))

class O_Point:  # Odd-row
    def __init__(self,q,r):
        self.q = q
        self.r = r

    def getKey(self):
        return self.q+","+self.r

    def toCube(self):
        x = self.q - (self.r - (self.r&1)) / 2
        z = self.r
        y = -x-z
        return C_Point(int(x),int(y),int(z))

    def toAxial(self):
        return toCube().toAxial()
'''
