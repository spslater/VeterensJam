import os, pygame, Globals

cs = Globals.CELL_SIZE
gt = Globals.GAME_TITLE

def draw(screen, font):
    screenWidth = screen.get_width()

    gameTitle = font.render(gt, 1, (255,255,255))
    titleWidth = gameTitle.get_width()
    offset = int(-(titleWidth - screenWidth)/2.0)
    screen.blit(gameTitle, (offset,cs))

    gameStart = font.render("Press ENTER to Start", 1, (255,255,255))
    startWidth = gameStart.get_width()
    offset = int(-(startWidth - screenWidth)/2.0)
    screen.blit(gameStart, (offset,cs*4))
