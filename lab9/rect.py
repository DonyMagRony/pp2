import pygame
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
                width = max(pos[0], sp[0]) - x
                height = max(pos[1], sp[1]) - y

                sc.fill(WHITE)
                pygame.draw.rect(sc, RED, pygame.Rect(x, y, width, height))
                pygame.display.update()
            else:
                    sp=None
                    
