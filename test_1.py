import pygame

from pygame.locals import *
pygame.init()
win = pygame.display.set_mode((500,500))
i = True
speed= 1
x=60
y=60
width=10
height=10
sec = 1
xr=50
yr=50
widthr=10
heightr=10
fall= False
fallr = False
delay = int(1000/60)
jump=False
isJump=0

def pos(x,y):
    pos=0
    if x <0:
        pos =1
    if x >500:
        pos =2
    if y <0:
        pos =3
    if y >500:
        pos =4
    return pos


    
    




while i:
    a = {"x":0, "y":0, "xr":0, "yr":0}
    pygame.time.delay(delay)
    win.fill((0,0,0))
    key = pygame.key.get_pressed()
    s = [abs(key[pygame.K_LEFT] - key[pygame.K_RIGHT]), abs(key[pygame.K_DOWN] - key[pygame.K_UP])]
    
    if key[pygame.K_LEFT]:
        a["x"] -=  speed
        a["xr"] -= speed * (x == xr+10 and abs(y - yr) < 10+s[1])
    if key[pygame.K_RIGHT]:
        a["x"] +=  speed
        a["xr"] += speed * (x == xr-10 and abs(y - yr) < 10+s[1])
    if y != 490 and not(y == yr-10 and abs(x - xr) < 10+s[0]) and not(jump):
        a["y"] +=  1
        
        
                    
    if yr != 490 and not(yr == y-10 and abs(xr - x) < 10+s[0]) :
        a["yr"] +=  speed
    if key[pygame.K_SPACE] and not(jump) and (y == 490 or (y == yr-10 and abs(x - xr) < 10+s[0])) :
        jump = True
    if jump :
        a["y"] -=  2.5
        isJump += 1
        if isJump >= 10:
            jump = False
            isJump = 0
            

    x += a["x"]
    y += a["y"]
    xr += a["xr"]
    yr += a["yr"]
    
    if sec ==  1:
        win.fill((0,0,0))
        pygame.draw.rect(win, (0,0,225),(x,y,width,height))
        pygame.draw.rect(win, (0,225,0),(xr,yr,widthr,heightr))
        posi = pos(x,y)
        if posi == 1:
            x = 500
            sec = 2
            
            
        if posi == 2:
            x = 0
            sec = 4
        if posi == 3:
            y = 500
            sec =3
        if posi == 4:
            y = 0
            sec =5
    if sec == 2:
        win.fill((0,0,0))
        pygame.draw.rect(win, (0,0,225),(x,y,width,height))
        
        posi = pos(x,y)
        

        if posi == 2:
            x = 0
            sec = 1
    if sec == 3:
        win.fill((0,0,0))
        pygame.draw.rect(win, (0,0,225),(x,y,width,height))
        posi = pos(x,y)
        

        if posi == 4:
            y = 0
            sec = 1
    if sec == 4:
        win.fill((0,0,0))
        pygame.draw.rect(win, (0,0,225),(x,y,width,height))
        posi = pos(x,y)
        

        if posi == 1:
            x = 500
            sec = 1
    if sec == 5:
        win.fill((0,0,0))
        pygame.draw.rect(win, (0,0,225),(x,y,width,height))
        posi = pos(x,y)
        

        if posi == 3:
            y = 500
            sec = 1
        
        
    for event in pygame.event.get():
        if event.type == QUIT:
            i = False
    pygame.display.update()

