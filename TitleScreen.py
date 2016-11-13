import os, pygame, Globals

cs = Globals.CELL_SIZE
gt = Globals.GAME_TITLE

def draw(screen, font):
    gameTitle = font.render(gt, 1, (255,255,255))
    titleWidth = gameTitle.get_width()
    screenWidth = screen.get_width()
    offset = int(-(titleWidth - screenWidth)/2.0)
    screen.blit(gameTitle, (offset,0))
