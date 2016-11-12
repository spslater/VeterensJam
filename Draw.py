import os, pygame, Globals


cs = Globals.CELL_SIZE


path = os.path.join("assets", "grass_01.png")
GRASS = pygame.image.load(path)

def draw(screen, grid, center):

    #s = pygame.transform.scale(GRASS, (Globals.CELL_SIZE, Globals.CELL_SIZE))
    #p = (0,0)
    #screen.blit(s,p)
    keyList = grid.getTable().keys()
    #print keyList
    for k in keyList:
        h = grid.getHex(k)
        p = h.getPos().toPixel().getPos()
        b = (center[0]+p[0]-cs,center[1]+p[1]-cs)
        #print "x: ", b[0]
        #print "y: ", b[1]
        s = pygame.transform.scale(GRASS, (cs*2, cs*2))
        #screen.blit(s, b)
        screen.blit(s, b)
