# Author: Sean Slater
# Version: 0.0.1
# Date: 2016-07-13

import sys, os, pygame, math, Globals, Hex, Point, Draw, Player, Control, TitleControl, TitleScreen

cs = Globals.CELL_SIZE
mr = Globals.MAP_RADIUS
bgc = (0,0,255)

def main():
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    gameFont = pygame.font.Font(os.path.join("assets", "font.ttf"),int(cs/1.5))
    m_width = int(round(((mr*cs*math.sqrt(3.0))+cs)*2))
    m_height = int(round(((mr*cs)+((math.ceil(mr/2.0)+1)*cs))*2))
    size = m_width, int(round(m_height*1.25))
    center = int(round(size[0]/2.0)), int(round((size[1]/2.0)/1.25))
    screen = pygame.display.set_mode(size)
    keys = pygame.key.get_pressed()
    grid = Hex.HexGrid(mr)
    p0 = Player.player(0,(mr*mr,mr*mr), grid)
    p1 = Player.player(1,(-mr,0), grid)
    p2 = Player.player(2,(mr,0), grid)
    players = [p0,p1,p2]

    background = pygame.Surface((m_width,m_height))

    scene = 0

    while True:
        screen.blit(background, (0,0))
        if scene == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    scene = TitleControl.keyProcess(event.key, scene)

            TitleScreen.draw(screen, gameFont)

        elif scene == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    Control.keyProcess(event.key, players, grid, screen)

            Draw.draw(screen, center, grid, players)

        pygame.display.flip()


if __name__ == '__main__':
    main()
