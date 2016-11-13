# Author: Sean Slater
# Version: 0.0.1
# Date: 2016-07-13

import sys, os, pygame, math, Globals, Hex, Point, Draw, Player, Control, TitleControl, TitleScreen

cs = Globals.CELL_SIZE
mr = Globals.MAP_RADIUS
bgc = (0,0,255)
ws = Globals.WINNING_SCORE

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

    game = Hex.initGame()

    background = pygame.Surface((m_width,m_height))
    scene = 0

    while True:
        if scene == 0:
            screen.blit(background, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    scene = TitleControl.keyProcess(event.key, scene)

            TitleScreen.draw(screen, gameFont)

        elif scene == 1:
            screen.blit(background, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    Control.keyProcess(event.key, game.players, game.grid, screen)
                    if event.key == pygame.K_t:
                        game.winner = 1
                        scene = 2

            for player in game.players:
                screen.blit(background, (0,0))
                if player.getScore() >= ws:
                    scene = 2
                    game.winner = player.num
                    player.setScore()

            Draw.draw(screen, center, game.grid, game.players)

        elif scene == 2:
            if event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_v:
                        scene = 0
                    if event.key == pygame.K_ESCAPE or key == pygame.K_SPACE:
                        sys.exit()
                elif event.type == pygame.QUIT:
                    sys.exit()

            game = Hex.initGame()
            screen.blit(background, (0,0))
            Draw.drawEnd(screen, game.players, game.winnner, gameFont)

        pygame.display.flip()


if __name__ == '__main__':
    main()
