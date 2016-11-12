# Author: Sean Slater
# Version: 0.0.1
# Date: 2016-07-13

import sys, os, pygame, math, Globals, Hex, Point, Draw

cs = Globals.CELL_SIZE
mr = Globals.MAP_RADIUS


def main():
    pygame.init()
    m_width = int(((mr*cs*math.sqrt(3.0))+cs)*2)
    #m_width = int((math.sqrt(3) * Globals.CELL_SIZE) * Globals.MAP_RADIUS)
    m_height = int(((mr*cs)+((math.ceil(mr/2.0)+1)*cs))*2)
    #m_height = int(((math.ceil(Globals.MAP_RADIUS / 2) * Globals.CELL_SIZE * 2) + (math.floor(Globals.MAP_RADIUS / 2) * Globals.CELL_SIZE) * 2))
    size = m_width, m_height
    #size = 600, 600
    center = int(size[0]/2.0), int(size[1]/2.0)
    print size, " : ", center
    screen = pygame.display.set_mode(size)
    keys = pygame.key.get_pressed()
    grid = Hex.HexGrid(mr)


    color = 54,216,212

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()


        #screen.fill(color)
        Draw.draw(screen, grid, center)
        pygame.display.flip()

if __name__ == '__main__':
    main()
