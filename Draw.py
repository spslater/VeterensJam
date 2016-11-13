import os, pygame, Globals


cs = Globals.CELL_SIZE

GRAS = pygame.image.load(os.path.join("assets", "grass.png"))
SAND = pygame.image.load(os.path.join("assets", "sand.png"))
STON = pygame.image.load(os.path.join("assets", "stone.png"))
DIRT = pygame.image.load(os.path.join("assets", "dirt.png"))
MARS = pygame.image.load(os.path.join("assets", "mars.png"))
NUM0 = pygame.image.load(os.path.join("assets", "text_0.png"))
NUM1 = pygame.image.load(os.path.join("assets", "text_1.png"))
NUM2 = pygame.image.load(os.path.join("assets", "text_2.png"))
NUM3 = pygame.image.load(os.path.join("assets", "text_3.png"))
NUM4 = pygame.image.load(os.path.join("assets", "text_4.png"))
NUM5 = pygame.image.load(os.path.join("assets", "text_5.png"))
NUM6 = pygame.image.load(os.path.join("assets", "text_6.png"))
NUM7 = pygame.image.load(os.path.join("assets", "text_7.png"))
NUM8 = pygame.image.load(os.path.join("assets", "text_8.png"))
NUM9 = pygame.image.load(os.path.join("assets", "text_9.png"))


DR1 = pygame.image.load(os.path.join("assets", "dRed1.png"))
DR2 = pygame.image.load(os.path.join("assets", "dRed2.png"))
DR3 = pygame.image.load(os.path.join("assets", "dRed3.png"))
DR4 = pygame.image.load(os.path.join("assets", "dRed4.png"))
DR5 = pygame.image.load(os.path.join("assets", "dRed5.png"))
DR6 = pygame.image.load(os.path.join("assets", "dRed6.png"))
DW1 = pygame.image.load(os.path.join("assets", "dWhi1.png"))
DW2 = pygame.image.load(os.path.join("assets", "dWhi2.png"))
DW3 = pygame.image.load(os.path.join("assets", "dWhi3.png"))
DW4 = pygame.image.load(os.path.join("assets", "dWhi4.png"))
DW5 = pygame.image.load(os.path.join("assets", "dWhi5.png"))
DW6 = pygame.image.load(os.path.join("assets", "dWhi6.png"))
DEM = pygame.image.load(os.path.join("assets", "dEmty.png"))


def getHexBackground(val):
    if val == 0:
        return GRAS
    elif val == 1:
        return SAND
    elif val == 2:
        return STON
    elif val == 3:
        return MARS
    else:
        return DIRT


def getResourceNum(val):
    if val == 1:
        return NUM1
    elif val == 2:
        return NUM2
    elif val == 3:
        return NUM3
    elif val == 4:
        return NUM4
    elif val == 5:
        return NUM5
    elif val == 6:
        return NUM6
    elif val == 7:
        return NUM7
    elif val == 8:
        return NUM8
    elif val == 9:
        return NUM9
    else:
        return NUM0


def getDieImg(val, player):
    if player == 0:
        return DEM
    elif val == 1:
        if player == 1:
            return DR1
        elif player == 2:
            return DW1
        else:
            print "bad player"
            return DIRT
    elif val == 2:
        if player == 1:
            return DR2
        elif player == 2:
            return DW2
        else:
            print "bad player"
            return DIRT
    elif val == 3:
        if player == 1:
            return DR3
        elif player == 2:
            return DW3
        else:
            print "bad player"
            return DIRT
    elif val == 4:
        if player == 1:
            return DR4
        elif player == 2:
            return DW4
        else:
            print "bad player"
            return DIRT
    elif val == 5:
        if player == 1:
            return DR5
        elif player == 2:
            return DW5
        else:
            print "bad player"
            return DIRT
    elif val == 6:
        if player == 1:
            return DR6
        elif player == 2:
            return DW6
        else:
            print "bad player"
            return DIRT
    else:
        print "bad die"
        return DIRT


def draw(screen, center, grid, players):
    keyList = grid.getTable().keys()
    for key in keyList:
        hexElem = grid.getHex(key)
        pixelPos = hexElem.getPos().toPixel().getPos()
        hexPos = (int(round(center[0]+pixelPos[0]-cs)), int(round(center[1]+pixelPos[1]-cs)))
        numPos = (int(round(center[0]+pixelPos[0]-cs*0.8)), int(round(center[1]+pixelPos[1]-cs*0.5)))
        bkImage = getHexBackground(hexElem.getTile())
        numImage = getResourceNum(hexElem.getResources())
        background = pygame.transform.scale(bkImage, (cs*2, cs*2))
        number = pygame.transform.scale(numImage, (int(round(cs*0.5)), int(round(cs*0.5))))
        screen.blit(background, hexPos)
        screen.blit(number, numPos)

        if hexElem.isOccupied() != 0:
            occImg = hexElem.getOccImg()
            occPos = (int(round(center[0]+pixelPos[0]-cs*0.35)), int(round(center[1]+pixelPos[1]-cs*0.05)))
            occupied = pygame.transform.scale(occImg, (int(round(cs*1.0)), int(round(cs*1.0))))
            screen.blit(occupied, occPos)

    for player in players:
        if player.num != 0:
            playPos = grid.getHex(player.getPos()).getPos().toPixel().getPos()
            realPos = (int(round(center[0]+playPos[0]-cs*0)), int(round(center[1]+playPos[1]-cs*0.75)))

            playImg = pygame.transform.scale(player.getPlayerImg(), (int(round(cs*1.0)), int(round(cs*1.0))))
            screen.blit(playImg, realPos)



def drawDie(screen, val, player):
    dieImg = pygame.transform.scale(getDieImg(val, player), (int(round(cs*1.0)), int(round(cs*1.0))))
    if player == 0:
        dieLoc01 = (int(round(cs*0.5)),int(round(screen.get_height()-cs*1.5)))
        dieLoc02 = (int(round(screen.get_width()-cs*1.5)),int(round(screen.get_height()-cs*1.5)))
        screen.blit(dieImg, dieLoc01)
        screen.blit(dieImg, dieLoc02)
    else:
        if player == 1:
            dieLoc = (int(round(cs*0.5)),int(round(screen.get_height()-cs*1.5)))
        elif player == 2:
            dieLoc = (int(round(screen.get_width()-cs*1.5)),int(round(screen.get_height()-cs*1.5)))
        screen.blit(dieImg, dieLoc)
