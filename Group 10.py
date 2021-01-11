#----------------Initialization + Countdown-------------------------------------
import pygame
import time
import os
pygame.mixer.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (192,192,192)
BEAUTIFUL_BLUE = (56, 215, 223)
DARK_BLUE = (65,105,225)
PURPLE = (75,0,130)
ORANGE = (255,99,71)
BLUE = (0,0,139)
DARK_PURPLE = (148,0,211)
SADDLE_BROWN = (139,69,19)
SIERRA = (160,82,45)
DARK_GREY = (105,105,105)

#Defining variables + Images
rect_x = 0
rect_y = 0
from pygame.locals import*
namek = pygame.image.load('Namek2.jpg')
spaceman = pygame.image.load('Spaceman2.jpg')
namekSpace = pygame.image.load('NamekGreenPlanet.jpg')
asteroid = pygame.image.load('Asteroid2.jpg')
asteroid2 = pygame.image.load('Asteroid3.jpg')
asteroid4 = pygame.image.load('Asteroid4.jpg')
sound=pygame.mixer.Sound('RocketBlast2.wav')
Galaxy = pygame.image.load('Galaxy.jpg')
Asteroid = pygame.image.load('AS12.png')
Asteroid2 = pygame.image.load('AS13.png')
sound3 = pygame.mixer.Sound('countdown.wav')
earth = pygame.image.load('earth.jpg')
#GAlaxy-------------------------------------------------------------------------
def backgroundGalaxy():
    screen.blit(Galaxy,(0,0))

#-------------------------------Rocket------------------------------------------
def rocket2(rect_x, rect_y):
    pygame.draw.polygon(screen, BLACK, [[350, 320+rect_y], [300, 340+rect_y], [400, 340+rect_y]])
    pygame.draw.polygon(screen, RED, [[299,200+rect_y],[299,290+rect_y],[270,290+rect_y]])
    pygame.draw.polygon(screen, RED, [[400,200+rect_y],[400,290+rect_y],[429,290+rect_y]])
    pygame.draw.rect(screen, GREY, [300, 120+rect_y, 100, 200])
    pygame.draw.polygon(screen, RED, [[300,120+rect_y], [350,40+rect_y], [400,120+rect_y]])
    pygame.draw.circle(screen,BLUE,(350, 190+rect_y),20)

#----------------------------Rocket---------------------------------------------
def rocket(rect_x,rect_y):
    pygame.draw.polygon(screen, BLACK, [[05+rect_x, 215+rect_y], [35+rect_x, 255+rect_y], [05+rect_x, 295+rect_y]])
    pygame.draw.rect(screen, GREY, [30+rect_x, 225+rect_y, 180, 60])
    pygame.draw.polygon(screen, RED, [(210+rect_x, 225+rect_y), (210+rect_x, 285+rect_y), (260+rect_x, 255+rect_y)])
    pygame.draw.circle(screen, BLUE, [160+rect_x,255+rect_y],20)
    pygame.draw.polygon(screen, RED, [(110+rect_x,225+rect_y), (55+rect_x,225+rect_y), (55+rect_x,195+rect_y)])
    pygame.draw.polygon(screen, RED, [(110+rect_x,285+rect_y), (55+rect_x,285+rect_y), (55+rect_x,315+rect_y)])
#-------------------------End Of Rocket----------------------------------------- 

#-------------------------BackGroundLaunch--------------------------------------
def backgroundLaunch(rect_x, rect_y):
        pygame.draw.circle(screen, WHITE, [350, 50], 6)
        pygame.draw.circle(screen, WHITE, [350, 50], 6)
        pygame.draw.circle(screen, WHITE, [450, 70], 3)     
        pygame.draw.circle(screen, WHITE, [550, 50], 4)
        pygame.draw.circle(screen, WHITE, [650, 70], 2)
        pygame.draw.circle(screen, WHITE, [750, 50], 5) 
        pygame.draw.circle(screen, WHITE, [200, 100], 2)
        pygame.draw.circle(screen, WHITE, [700, 300], 3)
        pygame.draw.circle(screen, WHITE, [200, 380], 2)
        pygame.draw.circle(screen, WHITE, [300, 100], 5)
        pygame.draw.circle(screen, WHITE, [400, 100], 6)
        pygame.draw.circle(screen, WHITE, [500, 100], 4)
        pygame.draw.circle(screen, WHITE, [250, 230], 3)
        pygame.draw.circle(screen, WHITE, [350, 200], 6)
        pygame.draw.circle(screen, WHITE, [200, 300], 2)
        pygame.draw.circle(screen, WHITE, [300, 300], 5)
        pygame.draw.circle(screen, WHITE, [400, 300], 6)
        pygame.draw.circle(screen, WHITE, [500, 300], 4)    
        pygame.draw.circle(screen, WHITE, [300, 430], 5)
        pygame.draw.circle(screen, WHITE, [400, 380], 6)
        pygame.draw.circle(screen, WHITE, [500, 430], 4)
        pygame.draw.circle(screen, WHITE, [600, 380], 2)
        pygame.draw.circle(screen, WHITE, [0, 230], 3)
        pygame.draw.circle(screen, WHITE, [40, 300], 5)     
        pygame.draw.circle(screen, WHITE, [80, 230], 3)
        pygame.draw.circle(screen, WHITE, [100, 400], 3)
        pygame.draw.circle(screen, WHITE, [160, 450], 6)
        pygame.draw.circle(screen, WHITE, [200, 300], 2)
        screen.blit(earth,(-600, 200))
#-------------------------EndOfBackgroundLaunch---------------------------------

#-------------------------Background Space--------------------------------------
def backgroundSpace(rect_x, rect_y):
        screen.fill(PURPLE)
        pygame.draw.circle(screen, WHITE, [350, 50], 6)
        pygame.draw.circle(screen, WHITE, [450, 70], 3)     
        pygame.draw.circle(screen, WHITE, [550, 50], 4)
        pygame.draw.circle(screen, WHITE, [650, 70], 2)
        pygame.draw.circle(screen, WHITE, [750, 50], 5) 
        pygame.draw.circle(screen, WHITE, [200, 100], 2)
        pygame.draw.circle(screen, WHITE, [700, 300], 3)
        pygame.draw.circle(screen, WHITE, [200, 380], 2)
        pygame.draw.circle(screen, WHITE, [300, 100], 5)
        pygame.draw.circle(screen, WHITE, [400, 100], 6)
        pygame.draw.circle(screen, WHITE, [500, 100], 4)
        pygame.draw.circle(screen, WHITE, [250, 230], 3)
        pygame.draw.circle(screen, WHITE, [350, 200], 6)
        pygame.draw.circle(screen, WHITE, [200, 300], 2)
        pygame.draw.circle(screen, WHITE, [300, 300], 5)
        pygame.draw.circle(screen, WHITE, [400, 300], 6)
        pygame.draw.circle(screen, WHITE, [500, 300], 4)    
        pygame.draw.circle(screen, WHITE, [300, 430], 5)
        pygame.draw.circle(screen, WHITE, [400, 380], 6)
        pygame.draw.circle(screen, WHITE, [500, 430], 4)
        pygame.draw.circle(screen, WHITE, [600, 380], 2)
        pygame.draw.circle(screen, WHITE, [0, 230], 3)
        pygame.draw.circle(screen, WHITE, [40, 300], 5)     
        pygame.draw.circle(screen, WHITE, [80, 230], 3)
        pygame.draw.circle(screen, WHITE, [100, 400], 3)
        pygame.draw.circle(screen, WHITE, [160, 450], 6)
        pygame.draw.circle(screen, WHITE, [200, 300], 2)
        pygame.draw.circle(screen, GREEN, [250, 400],100)
#--------------------------End Of Background Space------------------------------

# ----------------------------Asteroid Belt ------------------------------------
def asteroidBelt(rect_x, rect_y):
        screen.fill(DARK_PURPLE)
        screen.blit(asteroid,(30,3))
        screen.blit(asteroid2, (300,200))
#---------------------End of Asteroid Belt -------------------------------------

#-------------------------BackgroundLanding-------------------------------------
def backgroundLanding(rect_x, rect_y):
        screen.blit(namek,(0,0))        
#-------------------------EndOfBackgroundLanding--------------------------------
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("SHADMAN + WASEE'S ROCKET ANIMATION")
 
# Loop until the user clicks the close button.
done = False 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
count = 10
 # -------- Main Program Loop -----------
while not done:
     # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True                    #Keep all of this 
    sound3.play()
     # First, clear the screen to black. Don't put other drawing commands
     # above this, or they will be erased with this command.
    screen.fill(BLACK)
    sound=pygame.mixer.Sound('RocketBlast.wav')

    font = pygame.font.SysFont('Calibri', 200, True, False)

    if count<0:
        done=True
    else:
        text = font.render(str(count),True,WHITE)
    count=count-1
     # Put the image of the text on the screen at 300x150
    screen.blit(text, [300, 150])    
     
  
     # --- Go ahead and update the screen with what we've drawn.
    pygame.display.update()
  
     # --- Limit to 1 frame per second
    clock.tick(1)
    if count==0:
        done=True
#Reset--------------------------------------------------------------------------
done = False
rect_x = 0
rect_y = 0
count = 150
sound3.stop()
#New Scene----------------------------------------------------------------------
while not done:
        screen.fill(PURPLE)
        backgroundLaunch(0,0)
        sound.play()
        rocket2(rect_x,rect_y)
        rect_x +=3
        rect_y -=3
        clock.tick(60)
        pygame.display.update()
        if count<0:
                done=True
        else:
                text = font.render(str(count),True,WHITE)
        count=count-1        
        #Quit Button Code ------------------------------------------------------
        for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                        done=True # Flag that we are done so we exit this loop
#Reset--------------------------------------------------------------------------
done = False
rect_x = 0
rect_y = 0
count = 350

#Asteroid1 --------------------------------------------------------------------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if rocket== (rect_x+100,rect_y):
            pygame.mixer.stop()
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)
    sound2=pygame.mixer.Sound('prt.wav')
    sound2.play()        
    screen.blit(Galaxy,(0,0)) 
    screen.blit(Asteroid,(-(4)*rect_x+500,rect_y+300))
    screen.blit(Asteroid2,(-rect_x+700,rect_y+70))
    screen.blit(Asteroid2,(-(1.8)*rect_x+700,rect_y+400))
    screen.blit(Asteroid,(-(6)*rect_x,rect_y-40))
    clock.tick(60)
    pygame.display.update()
    if count<-1:
            done=True
    else:
            text = font.render(str(count),True,WHITE)
    count=count-1            
    
    #screen.fill(WHITE)
    rocket(rect_x,rect_y)
    # Move the rectangle starting point
    rect_x += 2
    rect_y += 0
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.update()


#Reset -------------------------------------------------------------------------
done = False
rect_x = 0
rect_y = 0
count = 70
#New Scene ---------------------------------------------------------------------
while not done:
        screen.fill(WHITE)
        screen.blit(namekSpace,[0,0])
        rocket(-300 + rect_x, rect_y)
        if rect_x < 200:
            rect_x += 3
        clock.tick(60)
        pygame.display.update()
        if count<0:
                done=True
        else:
                text = font.render(str(count),True,WHITE)
        count=count-1         
        #Quit Button Code ------------------------------------------------------
        for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                        done=True # Flag that we are done so we exit this loop
        

#Reset--------------------------------------------------------------------------
done = False
rect_x = 0
rect_y = -150
count = 150
sound.play()
#Landing scene -----------------------------------------------------------------
while not done:
        screen.fill(WHITE)
        screen.blit(namek,(0,0))
        rocket2(rect_x, rect_y)
        if rect_y<120:
                rect_y += 3      
        clock.tick(60)
        pygame.display.update()
        if count<0:
                done=True
        else:
                text = font.render(str(count),True,WHITE)
        count=count-1        
        #Quit Button Code ------------------------------------------------------
        for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                        done=True # Flag that we are done so we exit this loop

#Reset -------------------------------------------------------------------------
done = False
rect_x = 350
rect_y = 0
count = 100
sound.stop()
#Spaceman Scene ----------------------------------------------------------------
while not done:
        screen.fill(WHITE)
        screen.blit(namek,(0,0))
        rocket2(350, 120)
        screen.blit(spaceman,(rect_x, 390))
        if rect_x<500:
                rect_x += 3
        clock.tick(60)
        pygame.display.update()
        if count<0:
                done=True
        else:
                text = font.render(str(count),True,WHITE)
        count=count-1   