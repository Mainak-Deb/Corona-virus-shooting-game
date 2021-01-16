import pygame,sys
from pygame.locals import *
import random
from pygame import mixer
pygame.init()
screen=pygame.display.set_mode((800,600))


#icon
icon=pygame.image.load('virus.png')
pygame.display.set_icon(icon)


#game-name
pygame.display.set_caption("KILL CORONA")



#player
pli=pygame.image.load('human1.png')
pli=pygame.transform.scale(pli,(70,100))

#sanitizer
sanitizerpic=pygame.image.load('Hand-Sanitizer-Transparent.png')
sanitizerpic=pygame.transform.scale(sanitizerpic,(50,50))

#background
bg=pygame.image.load('ground1.png')
bg=pygame.transform.scale(bg,(800,600))
mixer.music.load('background.wav ')
mixer.music.play(-1)
#novel corona virus
coronapic=[]
corox=[]
coroy=[]
nc=[]
pncval=[]

for i in range(6):
    
    coronapic.append(pygame.image.load('virus.png'))
    coronapic[i]=pygame.transform.scale(coronapic[i],(50,50))
    corox.append(random.randint(2,700))
    coroy.append(random.randint(2,100))
    nc.append(4)
    pncval.append(4)



#functions...........................................#

#player
p1x=200
p1y=500


score=0
fonts1=pygame.font.Font('freesansbold.ttf',40)
fonts2=pygame.font.Font('freesansbold.ttf',50)

def killboard():
    s=fonts1.render("SCORE : "+str(score),True,(255, 13, 0))
    screen.blit(s,(0,0))
    
    
fontg=pygame.font.Font('freesansbold.ttf',80)
def gameover():
    g=fontg.render("GAME OVER",True,(0, 0, 0))
    g2=fonts2.render("YOUR SCORE: "+str(score),True,(0, 64, 255))

    screen.blit(g,(150,200))
    screen.blit(g2,(200,400))

def player(x,y):
    screen.blit(pli,(x,y))
    
#corona virus

   
def corona(x,y,i):
    screen.blit(coronapic[i],(x,y))  

#sanitizer

sy=450
scx=0
scy=40
sst="ready"

def sanitizer(x,y):
    global sst
    sst="fire"
    screen.blit(sanitizerpic,(x-20,y-20))  

def distancing(x1,y1,x2,y2):
    d=(((x1-x2)**2)+((y1-y2)**2))**(.5)
    if(d<50):
        return True
    else:
        return False















#running............#
cx=0
over=0





running=True
while running:
    screen.fill((66, 236, 245))
    screen.blit(bg,(0,0))  
    
    for event in pygame.event.get():
        if event.type == QUIT:
                pygame.quit()
                sys.exit()
                running=False
        if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    running=False
        if (event.type==pygame.KEYDOWN):
              if(event.key==pygame.K_RIGHT):
                  cx= 5
              elif(event.key==pygame.K_LEFT):
                  cx= -5
              elif(event.key==pygame.K_SPACE):
                  sanitizer(p1x,sy)
                
                
        if (event.type==pygame.KEYUP):
              if(event.key==pygame.K_RIGHT) or (event.key==pygame.K_LEFT) :
                  cx=0
             
        
   
    if(sy<0):
        sy=550
        sst="ready"
    if (sst =="fire"):
        sanitizersound=mixer.Sound('laser.wav')
        sanitizersound.play()
        sanitizer(p1x,sy)
        sy-=scy 
#enemy movement
    for i in range(6):
        attackedman=distancing(corox[i],coroy[i],p1x,p1y)
       
        if attackedman:
             ex=mixer.Sound('explosion.wav')
             ex.play()
             for j in range(6):
                 corox[j]=1000
                 coroy[j]=1000
                 
                 
             gameover()
             over=108
             break
             
            
        
        
        corox[i]+=nc[i]
        
        if(corox[i]>750):
             corox[i]=748
             nc[i]=(-1*pncval[i])
             coroy[i]=coroy[i]+50
             
        if(corox[i]<0):
             corox[i]=2
             pncval[i]+=1
             nc[i]=(pncval[i])
             coroy[i]=coroy[i]+50
             
    #collition
        collisiondestroy=distancing(corox[i],coroy[i],p1x,sy)
        if collisiondestroy:
            ex=mixer.Sound('explosion.wav')
            ex.play()
            sy=550
            sst="ready"
            score+=1
            pncval[i]=4
            corox[i]=random.randint(2,700)
            coroy[i]=random.randint(2,100)
        
            
            
            
        corona(corox[i],coroy[i],i)
    
    if (over==108):gameover()
    else:
        p1x+=cx 
        player(p1x,p1y)
    
        killboard()
        
    pygame.display.update()