import pygame 
from felo_game_functions import start, change_page

# globals / declarations
mainloop = True
b_w = 200   
b_l = 100
b_y = 800
white = [255, 255, 255] 
black = [0, 0, 0]
#options = 0 
raisin = [29, 30, 44]
grape = [172, 159, 187]
current_page = 2
#all possible paths 
paths = {2: [3], 3: [4], 4: [5], 5: [6], 6: [9, 33], 9: [48], 48: [33], 33: [60, 75],
         60: [], 75: [94], 94: [51], 51: [22, 68, 105, 113], 22: [], 68: [87],
         87: [81, 106], 81: [56], 106: [], 56: [65],
         49: [89], 89: [53], 53: [99], 99: [64, 130], 64: [20],
         130: [12], 20: [12], 12: [40], 40: [101, 67], 67: [78], 78: [55],
         55: [127, 118], 127: [21], 118: [], 21: [72], 72: [96], 96: [125, 74],
         47: [55], 117: [], 124: [112], 112: [93], 93: [], 113: [43], 43: [38],
         38: [97, 8], 8: [82], 82: [88], 88: [], 97: [56],
         65: [36, 23], 23: [], 36: [49], 105: [28], 28: [46], 46: [107],
         107: [80], 80: [56, 116], 116: [123], 123: [17], 17: [39, 62], 39: [54],
         54: [77], 77: [25, 100, 119], 25: [66], 66: [], 119: [], 100: [30, 14],
         14: [92], 92: [85], 85: [], 30: [42], 42: [73, 102], 102: [27],
         27: [44], 44: [90], 90: [109], 109: [3], 73: [19], 19: [11, 35, 58],
         58: [71], 71: [], 35: [115], 115: [129], 129: [], 11: [84], 84: [79],
         79: [34], 34: [86], 86: [98], 98: [15, 29, 57], 29: [], 15: [59],
         59: [50], 50: [103], 103: [83], 83: [18], 18: [], 57: [31], 31: [],
         62: [37, 10], 37: [], 10: [76], 76: [131], 131: [108], 108: [52, 13],
         13: [], 52: [24], 24: [], 125: [61], 61: [91], 91: [111]}

class Button(pygame.Rect):
    def __init__(self, x, y, length, width, idx):
        super().__init__(x, y, length, width)
        self.idx = idx
        self.on_screen = False
    
    def show_options(self):
        pygame.font.init()
        font = pygame.font.SysFont('', 50,  True)
        text = font.render(str(paths[current_page][self.idx]), 1, black)
        textpos = text.get_rect(centerx = (self.x + self.width/2), centery = self.y + self.height/2)
        screen.blit(text, (textpos))

# initializations
screen=pygame.display.set_mode([1920, 1080], pygame.RESIZABLE)
pygame.init()

# rectangles declarations
bg = pygame.Rect(0, 0, screen.get_width(), screen.get_height()) # bg rectangle (used to find center the buttons)
b_x = bg.centerx

rectB = Button(b_x - b_w * 2, b_y, b_w, b_l, 1) # 1 option
rectA = Button(b_x - b_w / 2, b_y, b_w, b_l, 0) #3a option
rectC = Button(b_x + b_w, b_y, b_w, b_l, 2) # 3b option

rect1 = Button((b_x + b_w / 2), b_y, b_w, b_l, 0) # 2a option
rect2 = Button((b_x - b_w - b_w / 2), b_y, b_w, b_l, 1) # 2b option 

rect3 = Button((b_x - b_w * 3.5 ), b_y, b_w, b_l, 2) # 4a option
rect4 = Button((b_x + b_w * 2.5), b_y, b_w, b_l, 3)# 4b

rect_list = [rectA, rectB, rectC, rect1, rect2, rect3, rect4] 

while mainloop:
    for rect in rect_list:
        rect.on_screen = False

    mouse = pygame.mouse.get_pos() # get the mouse x and y coord 
    options = len(paths[current_page]) # num of options on the page
    screen.fill(raisin) #colours for bg

    if paths[current_page]:
        if options == 2 or options == 4: # check if 2 or 4
            pygame.draw.rect(screen, (grape), rect1) # always draws the 2 middle squares
            rect1.on_screen = True
            rect1.show_options()
            
            pygame.draw.rect(screen, (grape), rect2) 
            rect2.on_screen = True
            rect2.show_options()
            
            if options == 4:
                pygame.draw.rect(screen, (grape), rect3) # if 4 draws 2 outer squares
                rect3.on_screen = True
                rect3.show_options()
                
                pygame.draw.rect(screen, (grape), rect4)
                rect4.on_screen = True
                rect4.show_options()
        elif current_page == 3:
            pygame.draw.rect(screen, (grape), rect4)
            rect4.idx = 0
            rect4.on_screen = True
            rect4.show_options()
        
        else:
            pygame.draw.rect(screen, (grape),rectA) # else (odd), draws the middle odd button
            rectA.on_screen = True
            rectA.show_options()
            if options == 3: # if 3 draws 2 outer squares
                pygame.draw.rect(screen, (grape),rectB) 
                rectB.on_screen = True
                rectB.show_options()

                pygame.draw.rect(screen, (grape),rectC)
                rectC.on_screen = True
                rectC.show_options()
    else:
        screen.fill(black) #colours for bg                
    
    start(current_page, screen) # printing the current_page
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            for rect in rect_list:# collision cehcker
                if rect.collidepoint(mouse[0], mouse[1]) and rect.on_screen: 
                    current_page = change_page(paths, current_page, rect.idx)

        if event.type == pygame.QUIT:
            mainloop = False #quitting

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False #quitting with esc

    pygame.display.flip() # updating the display

pygame.quit() # quit
