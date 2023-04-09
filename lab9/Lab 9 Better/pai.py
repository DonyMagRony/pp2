import pygame
import random
import math


screen = pygame.display.set_mode((900, 700))


pygame.display.set_caption('Paint')

draw_on = False
last_pos = (0, 0)
blockwidth = 50
radius = 5
#colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)

#collors buttons allocation
COLOR_BUTTONS = [
    {"color": RED, "rect": pygame.Rect(10, 10, 50, 50)},
    {"color": BLACK, "rect": pygame.Rect(70, 10, 50, 50)},
    {"color": YELLOW, "rect": pygame.Rect(130, 10, 50, 50)},
    {"color": GREEN, "rect": pygame.Rect(190, 10, 50, 50)},
    {"color": BLUE, "rect": pygame.Rect(250, 10, 50, 50)},
    {"color": PURPLE, "rect": pygame.Rect(310, 10, 50, 50)}
]
#loading images
eraser = pygame.image.load('image/eraser.jpg')
rectan = pygame.image.load('image/rect.jpg')
trian = pygame.image.load('image/triangle.png')

#transforming images 
eraser_img_resize = pygame.transform.scale(eraser, (blockwidth, blockwidth))
rectan_img_resize = pygame.transform.scale(rectan, (blockwidth, blockwidth))
trian_img_resize = pygame.transform.scale(trian, (blockwidth, blockwidth))

#buttons allocations
eraser_rect = pygame.Rect(360, 10, 50, 50)
rectan_rect = pygame.Rect(410, 10, 50, 50)
trian_rect = pygame.Rect(460, 10, 50, 50)

draw_rect = False
#draw rect for color button
def drawRect(canvas, color, rect_start_pos, rect_end_pos, radius=1):
    pygame.draw.rect(canvas, color, (rect_start_pos[0], rect_end_pos[0]))


#drawing circles
def roundline(canvas, color, start, end, radius=1) :
    Xaxis = end[0] - start[0]
    Yaxis = end[1] - start[1]
    dist = max(abs(Xaxis), abs(Yaxis))
    for i in range(dist) :
        x = int(start[0] + float(i) / dist * Xaxis)
        y = int(start[1] + float(i) / dist * Yaxis)
        pygame.draw.circle(canvas, color, (x, y), radius)



color = 'BLACK'
screen.fill((255,255,255))
mode="none"
sp=None
x=0

try:
    while True:

        e = pygame.event.wait()
        if e.type == pygame.QUIT:
            raise StopIteration
        
        if e.type == pygame.MOUSEBUTTONDOWN:
            #condition to change color if eraser was choosed
            if eraser_rect.collidepoint(e.pos):
                color = WHITE
            #conditions to mode change if figure choosen
            if rectan_rect.collidepoint(e.pos):
                mode="rectangle"
            if trian_rect.collidepoint(e.pos):
                mode="triangle"
            for button in COLOR_BUTTONS:
                if button["rect"].collidepoint(e.pos):
                    color = button['color']

        #if rectangle mode choosed starts rect draw
        if mode=="rectangle":
              #defining is mouse get pressed 
            pressed=pygame.mouse.get_pressed()
            if pressed:
                #defining positions of click
                pos=pygame.mouse.get_pos()
            if sp is None:
                   #changing draw status and creating list with coordinates
                flStartDraw=True
                sp = e.pos
                #if left click is done starts drawing
            elif e.type == pygame.MOUSEBUTTONDOWN and e.button==1:
                if flStartDraw:
                    pos = e.pos
                    #defining minimal coordinates
                    x, y = min(sp[0], pos[0]), min(sp[1], pos[1])
                    #defining width and height
                    width = max(pos[0], sp[0]) - x
                    height = max(pos[1], sp[1]) - y
                    pygame.draw.rect(screen, RED, pygame.Rect(x, y, width, height))
                    pygame.display.update()
                    #redefing mode ,stoping drawing
                    mode="none"
                    flStartDraw=False
                else:
                        sp=None
        elif mode=="triangle":
            #defining is mouse get pressed 
            pressed=pygame.mouse.get_pressed()
            if pressed:
                #defining positions of click
                pos=pygame.mouse.get_pos()
            if sp is None:
                #changing draw status and creating list with coordinates
                flStartDraw=True
                sp = e.pos
                #if left click is done starts drawing
            elif e.type == pygame.MOUSEBUTTONDOWN and e.button==1:
                if flStartDraw:
                    pos = e.pos
                    x, y = min(sp[0], pos[0]), min(sp[1], pos[1])
                    x1,y1= max(pos[0], sp[0]),max(pos[1], sp[1])
                    #defining distance
                    distance = math.sqrt((x1 - x)**2 + (y1 - y)**2)
                    # calculate the angle between the two points
                    angle = 60
                    # calculate the coordinates of the third point (the first one)
                    x2 = x1 - distance * math.cos(angle - (1 * math.pi / 3))
                    y2 = y1 - distance * math.sin(angle - (1 * math.pi / 3))
                    #drawing lines
                    pygame.draw.lines(screen,BLUE,True,[(x,y),(x1,y1),(x2,y2)],2) 
                    pygame.display.update()
                    #redefinition of mode ,stoping drawing
                    mode="none"
                    flStartDraw=False
                else:
                        sp=None
        else:           
            if e.type == pygame.MOUSEBUTTONDOWN:
                # Selecting Color Code
                # Draw a single circle wheneven mouse is clicked down.
                pygame.draw.circle(screen, color, e.pos, radius)
                draw_on = True
            if e.type == pygame.MOUSEBUTTONUP:
                draw_on = False
            if e.type == pygame.MOUSEMOTION:
                if draw_on:
                    pygame.draw.circle(screen, color, e.pos, radius)
                    roundline(screen, color, e.pos, last_pos, radius)
                last_pos = e.pos

            #Drawing color buttons
            for button in COLOR_BUTTONS:
                pygame.draw.rect(screen, button["color"], button["rect"])
            
            #creating image blocks of eraser ,rectangle,triangle
            screen.blit(eraser_img_resize, (370, 10))
            screen.blit(rectan_img_resize,(420, 10))
            screen.blit(trian_img_resize,(470, 10))
            pygame.display.flip()
except StopIteration:
    pass


pygame.quit()