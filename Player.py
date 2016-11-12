import pygame, os, random, sys

class player:
    def __init__(self, num, pos, grid, score = 0):
        self.num = num
        self.pos = pos
        self.score = score
        self.playerImage = self.setPlayerImage()
        self.claimedImage = self.setClaimedImage()

        try:
            grid.getHex(self.getPos()).setPlayerOn(self.num)
        except KeyError:
            print "Bad Player Loc"


    def addScore(self, val):
        self.score += val

    def movePlayer(self,nPos):
        self.pos = nPos

    def setPos(self,grid,x,y):
        try:
            newPos = self.pos[0]+x,self.pos[1]+y
            hexElem = grid.getHex(str(newPos[0])+","+str(newPos[1]))
            if hexElem.getPlayerOn() == 0:
                grid.getHex(self.getPos()).setPlayerOn(0)
                self.pos = self.pos[0]+x,self.pos[1]+y
                hexElem.setPlayerOn(self.num)

            else:
                print "Hex occupied by player"
        except KeyError:
            print "Invalid Move"


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


    def playTurn(self,grid, players):
        dice = random.randint(1,6)
        #print "Die Roll: ", dice
        hexElem = grid.getHex(str(self.getPos()))
        print hexElem.isOccupied()
        if hexElem.isOccupied() != self.num:
            hexElem.setResources(dice)
        else:
            print "Pick another space"
        #print "resource: ", hexElem.getResources()
        if hexElem.getResources() <= 0:
            hexElem.resetResources()
            if hexElem.isOccupied() != 0 and hexElem.isOccupied() != self.num:
                players[hexElem.isOccupied()].addScore(-dice)
                hexElem.setOccupied(0)
            elif hexElem.isOccupied() == 0:
                hexElem.setOccupied(self.num)
                hexElem.setOccImg(self.getClaimedImg())
                self.addScore(dice)
        #print "Resource Value: ", hexElem.getResources()
