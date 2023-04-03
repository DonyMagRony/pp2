import pygame,math
pygame.init()
W=600
H=600
sc = pygame.display.set_mode((W,H))
WHITE =(255,255,255)
BLUE=(0,0,255)
GREEN=(0,255,0)
RED=(255,0,0)

FPS=60
clock=pygame.time.Clock()

sp= None
sc.fill(WHITE)
pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    pressed=pygame.mouse.get_pressed()
    if pressed[0]:
        pos=pygame.mouse.get_pos()
        if sp is None:
            flStartDraw=True
            sp = event.pos
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
            if flStartDraw:
                pos = event.pos
                x, y = min(sp[0], pos[0]), min(sp[1], pos[1])
                x1,y1= max(pos[0], sp[0]),max(pos[1], sp[1])
                distance = math.sqrt((x1 - x)**2 + (y1 - y)**2)
                # calculate the angle between the two points
                angle = 60
                # calculate the coordinates of the third point (the first one)
                x2 = x1 + distance * math.cos(angle - (1 * math.pi / 3))
                y2 = y1 + distance * math.sin(angle - (1 * math.pi / 3))
                sc.fill(WHITE)
                pygame.draw.line(sc,BLUE,(x,y),(x1,y1))
                pygame.draw.line(sc,BLUE,(x1,y1),(x2,y2))
                pygame.draw.line(sc,BLUE,(x,y),(x2,y2))
                pygame.display.update()
            else:
                    sp=None
pygame.quit()