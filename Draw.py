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


def getResourceNUm(val):
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

def draw(screen, grid, center):
    keyList = grid.getTable().keys()
    for key in keyList:
        hexElem = grid.getHex(key)
        pixelPos = hexElem.getPos().toPixel().getPos()
        hexPos = (int(round(center[0]+pixelPos[0]-cs)), int(round(center[1]+pixelPos[1]-cs)))
        numPos = (int(round(center[0]+pixelPos[0]-cs*0.5)), int(round(center[1]+pixelPos[1]-cs*0.5)))
        bkImage = getHexBackground(hexElem.getTile())
        numImage = getResourceNUm(hexElem.getValue())
        background = pygame.transform.scale(bkImage, (cs*2, cs*2))
        number = pygame.transform.scale(numImage, (cs, cs))
        screen.blit(background, hexPos)
        screen.blit(number, numPos)
