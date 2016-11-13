import pygame, sys

def keyProcess(key, s):
    if key == pygame.K_g:
        return 1
    elif key == pygame.K_ESCAPE or key == pygame.K_SPACE:
        sys.exit()
        return 0
    else:
        return 0
