# Author: Sean Slater
# Version: 0.0.1
# Date: 2016-07-13

import sys, os, pygame, math, Globals, Hex, Point, Draw

cs = Globals.CELL_SIZE
mr = Globals.MAP_RADIUS


def main():
    pygame.init()
    m_width = int(round(((mr*cs*math.sqrt(3.0))+cs)*2))
    m_height = int(round(((mr*cs)+((math.ceil(mr/2.0)+1)*cs))*2))
    size = m_width, m_height
    center = int(round(size[0]/2.0)), int(round(size[1]/2.0))
    screen = pygame.display.set_mode(size)
    keys = pygame.key.get_pressed()
    grid = Hex.HexGrid(mr)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()


        Draw.draw(screen, grid, center)
        pygame.display.flip()

if __name__ == '__main__':
    main()
