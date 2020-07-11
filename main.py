import pygame
from sort_tools import *
from pygame.locals import *

width = 900
height = 600

screen = pygame.display.set_mode((width, height))
pygame.init()

list = get_list(150, 0, height)
index = 0
end = 1

clock = pygame.time.Clock()
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            break

    if index < len(list)-end:
        index = index + 1
    else:
        index = 1
        end += 1

    sort(list, index)
    show(screen, width, height, list, index)

    pygame.display.flip()
