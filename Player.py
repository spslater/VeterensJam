import pygame, os, random

class player:
    def __init__(self, num, pos, score = 0):
        self.num = num
        self.pos = pos
        self.score = score
        self.playerImage = self.setPlayerImage()
        self.claimedImage = self.setClaimedImage()

    def addScore(self, val):
        self.score += val

    def movePlayer(self,nPos):
        self.pos = nPos

    def setPos(self,x,y):
        self.pos = self.pos[0]+x,self.pos[1]+y

    def getPos(self):
        return str(self.pos[0])+","+str(self.pos[1])

    def setPlayerImage(self):
        if self.num == 1:
            return pygame.image.load(os.path.join("assets", "playerBlue.png"))
        elif self.num == 2:
            return pygame.image.load(os.path.join("assets", "playerGreen.png"))
        else:
            return pygame.image.load(os.path.join("assets", "playerBlack.png"))

    def getPlayerImg(self):
        return self.playerImage

    def setClaimedImage(self):
        if self.num == 1:
            return pygame.image.load(os.path.join("assets", "claimedBlue.png"))
        elif self.num == 2:
            return pygame.image.load(os.path.join("assets", "claimedGreen.png"))
        else:
            return pygame.image.load(os.path.join("assets", "claimedBlack.png"))

    def getClaimedImg(self):
        return self.claimedImage


    def playTurn(self,grid):
        die = random.randint(1,6)
        #print "Die Roll: ", die
        hexElem = grid.getHex(str(self.getPos()))
        print hexElem.isOccupied()
        if hexElem.isOccupied() != self.num:
            hexElem.setResources(die)
        #print "resource: ", hexElem.getResources()
        if hexElem.getResources() <= 0:
            hexElem.resetResources()
            if hexElem.isOccupied() != 0 and hexElem.isOccupied() != self.num:
                hexElem.setOccupied(0)
            elif hexElem.isOccupied() == 0:
                hexElem.setOccupied(self.num)
                hexElem.setOccImg(self.getClaimedImg())
        #print "Resource Value: ", hexElem.getResources()
