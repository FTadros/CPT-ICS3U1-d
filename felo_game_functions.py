import pygame
import os
def start(page, screen):
    if type(page) is not str:
        page -= 2
        page = str(page)
    count = 0
    pygame.font.init()
    font = pygame.font.SysFont('', 32)
    working_directory = os.getcwd()
    file_path = (working_directory + "/text/text (" + page + ").txt")
    with open(file_path, encoding="utf8") as f:
        for line in f:
            count += 35
            text = font.render(line.strip(), 1, [89, 101, 111])
            textpos = text.get_rect(centerx = (screen.get_width()/2), centery = count)
            screen.blit(text, textpos) 

def change_page(paths, current_page, idx):
    if (paths[current_page]):  # while the player has not reached a page without anymore paths
        print(current_page)
        current_page = paths[current_page][idx]
    return current_page