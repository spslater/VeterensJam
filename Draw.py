import os, pygame, Globals


cs = Globals.CELL_SIZE


path = os.path.join("assets", "grass_06.png")
GRASS = pygame.image.load(path)

def draw(screen, grid, center):
    keyList = grid.getTable().keys()
    for k in keyList:
        h = grid.getHex(k)
        p = h.getPos().toPixel().getPos()
        b = (center[0]+p[0]-cs , center[1]+p[1]-cs)
        s = pygame.transform.scale(GRASS, (cs*2, cs*2))
        screen.blit(s, b)
