from random import randint, shuffle
import pygame


def get_list(lenght, init, limit, aesthetic=False):
    if not aesthetic:
        return [randint(init, limit) for _ in range(lenght)]
    list = [i for i in range(init, limit, lenght)]
    shuffle(list)
    return list

def show(screen, width, height, list, atual):
    bar_width = width//len(list)
    for i in range(len(list)):
        pos = i*bar_width, height-list[i]
        color = list[i] * 200//height, 15, list[i] * 10//height
        color = (255, 255, 255) if i != atual else (255, 0, 0)
        pygame.draw.rect(screen, color, (pos, (bar_width, height-pos[1])))



def sort(list, index):
    if list[index-1] > list[index]:
        list[index-1], list[index] = list[index], list[index-1]



if __name__ == '__main__':
    pass
