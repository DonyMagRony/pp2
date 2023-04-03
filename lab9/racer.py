import pygame, random, sys, os, time
from pygame.locals import *

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOR = (0, 0, 0)
FPS = 40
BADDIEMINSIZE = 10
BADDIEMAXSIZE = 40
BADDIEMINSPEED = 8
BADDIEMAXSPEED = 8
ADDNEWBADDIERATE = 6
PLAYERMOVERATE = 5
count = 3


def terminate() :
    pygame.quit()
    sys.exit()


def waitForPlayerToPressKey() :
    while True :
        for event in pygame.event.get() :
            if event.type == QUIT :
                terminate()
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :  
                    terminate()
                return


def playerHasHitBaddie(playerRect, baddies) :
    for b in baddies :
        if playerRect.colliderect(b['rect']) :
            return True
    return False


def drawText(text, font, surface, x, y) :
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('car race')
pygame.mouse.set_visible(False)

font = pygame.font.SysFont(None, 30)

gameOverSound = pygame.mixer.Sound('music/crash.mp3')
pygame.mixer.music.load('music/car.mp3')
laugh = pygame.mixer.Sound('music/laugh.mp3')

playerImage = pygame.image.load('image/car1.png')
car3 = pygame.image.load('image/car3.png')
car4 = pygame.image.load('image/car4.png')
playerRect = playerImage.get_rect()
baddieImage = pygame.image.load('image/car2.png')
sample = [car3, car4, baddieImage]
wallLeft = pygame.image.load('image/left.png')
wallRight = pygame.image.load('image/right.png')
coin = pygame.image.load('image/coin.png')
#####coin image uploaded 


drawText('Press any key to start the game.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3))
drawText('And Enjoy', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3) + 30)
pygame.display.update()
waitForPlayerToPressKey()
zero = 0
if not os.path.exists("data/save.dat") :
    f = open("data/save.dat", 'w')
    f.write(str(zero))
    f.close()
v = open("data/save.dat", 'r')
topScore = int(v.readline())
v.close()
while (count > 0) :
    baddies = []
    score = 0
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)
    
#####first coin coordiantes and exsistance coins counters
    coin_x,coin_y=random.randrange(0.2*WINDOWWIDTH,0.6*WINDOWWIDTH),0
    coin_exsist=True
    coins=0
    speeder=0
    while True : 
        score += 1  
        
####coin movement and appearing of new coin if previous was remved
        coin_y+=BADDIEMINSPEED
        if coin_exsist==False:
            coin_x,coin_y=random.randrange(0.2*WINDOWWIDTH,0.6*WINDOWWIDTH),0
            coin_exsist=True   
        

        for event in pygame.event.get() :

            if event.type == QUIT :
                terminate()

            if event.type == KEYDOWN :
                if event.key == ord('z') :
                    reverseCheat = True
                if event.key == ord('x') :
                    slowCheat = True
                if event.key == K_LEFT or event.key == ord('a') :
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == ord('d') :
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == ord('w') :
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == ord('s') :
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP :
                if event.key == ord('z') :
                    reverseCheat = False
                    score = 0
                if event.key == ord('x') :
                    slowCheat = False
                    score = 0
                if event.key == K_ESCAPE :
                    terminate()

                if event.key == K_LEFT or event.key == ord('a') :
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d') :
                    moveRight = False
                if event.key == K_UP or event.key == ord('w') :
                    moveUp = False
                if event.key == K_DOWN or event.key == ord('s') :
                    moveDown = False

    
        if not reverseCheat and not slowCheat :
            baddieAddCounter += 1
        if baddieAddCounter == ADDNEWBADDIERATE :
            baddieAddCounter = 0
            baddieSize = 30
            newBaddie = {'rect' : pygame.Rect(random.randint(140, 485), 0 - baddieSize, 23, 47),
                         'speed' : random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                         'surface' : pygame.transform.scale(random.choice(sample), (23, 47)),
                         }
            baddies.append(newBaddie)
            sideLeft = {'rect' : pygame.Rect(0, 0, 126, 600),
                        'speed' : random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface' : pygame.transform.scale(wallLeft, (126, 599)),
                        }
            baddies.append(sideLeft)
            sideRight = {'rect' : pygame.Rect(497, 0, 303, 600),
                         'speed' : random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                         'surface' : pygame.transform.scale(wallRight, (303, 599)),
                         }
            baddies.append(sideRight)
       
        if moveLeft and playerRect.left > 0 :
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH :
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0 :
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT :
            playerRect.move_ip(0, PLAYERMOVERATE)

        for b in baddies :
            if not reverseCheat and not slowCheat :
                b['rect'].move_ip(0, b['speed'])
            elif reverseCheat :
                b['rect'].move_ip(0, -5)
            elif slowCheat :
                b['rect'].move_ip(0, 1)

        for b in baddies[:] :
            if b['rect'].top > WINDOWHEIGHT :
                baddies.remove(b)

#####removing coin if it is below window       
        if coin_y>WINDOWHEIGHT:
                coin_exsist=False
        
        windowSurface.fill(BACKGROUNDCOLOR)

#### coin appearing on window
        windowSurface.blit(coin,(coin_x,coin_y))
    
        drawText('Score: %s' % (score), font, windowSurface, 128, 0)
        drawText('Top Score: %s' % (topScore), font, windowSurface, 128, 20)
        drawText('Rest Life: %s' % (count), font, windowSurface, 128, 40)
        drawText('Coins %s' % (coins), font, windowSurface, 128, 60)
        windowSurface.blit(playerImage, playerRect)

        for b in baddies :
            windowSurface.blit(b['surface'], b['rect'])

        pygame.display.update()

        
        if playerHasHitBaddie(playerRect, baddies) :
            if score > topScore :
                g = open("data/save.dat", 'w')
                g.write(str(score))
                g.close()
                topScore = score
            break
####if coin was collected removes coin and increases counters
        if playerRect.colliderect((coin_x,coin_y,30,28)):
            coin_exsist=False
            coins+=1
            speeder+=1
#### if 5 coin collected increases speed range
        if speeder==5:
            BADDIEMINSPEED+=2
            BADDIEMAXSPEED+=2
            speeder=0

        mainClock.tick(FPS)

 
    pygame.mixer.music.stop()
    count = count - 1
    gameOverSound.play()
    time.sleep(1)
    if (count == 0) :
        laugh.play()
        drawText('Game over'+coins, font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
        drawText('Press any key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 30)
        pygame.display.update()
        time.sleep(2)
        waitForPlayerToPressKey()
        count = 3
        gameOverSound.stop()