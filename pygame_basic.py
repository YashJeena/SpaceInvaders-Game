import pygame #importing pygame module
import random #importing random module
import math # importing math module
from pygame import mixer #import sound module from pygame



screen=pygame.display.set_mode((800,600)) #setting up the screen
backgroundimg=pygame.image.load('background.jpg') # Loading Background image
backgroundsound=mixer.music.load('game sound.mp3') # Loading background sound
mixer.music.play(-1) # playing background sound continiously

#Title and Icon
pygame.display.set_caption('SpaceX GAME')
icon=pygame.image.load('logo.png')
pygame.display.set_icon(icon)



#Player
playerimg=pygame.image.load('player.png')
playerX=370
playerY=480
playerX_change=0
playerY_change=0

#function player
def player(x,y):
    screen.blit(playerimg,(x,y)) # drawing player to screen

#Enemy
#creating multiple enemeies
num=6  # no of enemies
enemyimg=[]
enemyX=[]
enemyY=[]
for i in range(0,num):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(0)

enemyX_change=0
enemyY_change=0.05



#function enemy
def enemy(i,a,b):
    screen.blit(enemyimg[i],(a,b)) # drawing enemy to screen

#Bullet
bulletimg=pygame.image.load('bullet.png')
bulletX=370
bulletY=480
bulletX_change=0
bulletY_change=5
state=0  # state=0 means ready to fire/state=1 means fired

#function bullet
def bullet(p,q):    # Function bullet to fire bullet in screen
    screen.blit(bulletimg,(p,q)) # drawing bullet to the screen

#function collision between bullet and enemy
def collision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt((math.pow((enemyX-bulletX),2))+(math.pow((enemyY-bulletY),2))) # distance between bullet and enemy
    if distance<25:
        return True 
    else:
        return False

# Displaying Score
score_val=0
scoreX=10
scoreY=10
font=pygame.font.Font(None,50)

#function show_score
def show_score(g,h):
    score=font.render("score: "+str(score_val),True,(255,255,255))
    screen.blit(score,(g,h))

#game over function
gameoverfont=pygame.font.Font(None,100)
final_scorefont=pygame.font.Font(None,75)
gameoverX=200
gameoverY=250
def game_over():
    over=gameoverfont.render("GAME OVER",True,(255,255,255))
    fscore=final_scorefont.render("SCORE: "+str(score_val),True,(255,255,255))
    screen.blit(fscore,(250,350))
    screen.blit(over,(gameoverX,gameoverY))
    pygame.mixer.music.stop()  # Stop the background music

    


# Game loop
running=True
while running:

    # Show the play game screen before starting the game
   

    screen.fill((0,255,255)) # Background colour(red,green,blue)
    screen.blit(backgroundimg,(0,0))  # Setting Background image
    for event in pygame.event.get():
        # Quit control
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
        
        # KEYBOARD input controls
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=playerX_change-0.5
            if event.key==pygame.K_RIGHT:
                playerX_change=playerX_change+0.5
            if event.key==pygame.K_UP:
                playerY_change=playerY_change-0.5
            if event.key==pygame.K_DOWN:
                playerY_change=playerY_change+0.5
            if event.key==pygame.K_SPACE:
                if state==0: # if bullet ready to fire then only fire
                    state=1  # bullet fired
                    bulletX=playerX+16 # postion of bullet in x direction when state=1
                    bulletY=playerY+10 # position of bullet in Y direction when state=1
                    bullet(playerX,playerY) # bullet appears on the position of spaceship
                    bullet_sound=mixer.Sound('laser sound.mp3') # loading bullet sound
                    bullet_sound.play() # playing bullet sound
                                    
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                playerY_change=0
                    
                
    playerX=playerX+playerX_change # Movement of player
    playerY=playerY+playerY_change

    for i in range(0,num):
        enemyX[i]=enemyX[i]+enemyX_change # Movement of enemy
        enemyY[i]=enemyY[i]+enemyY_change

        #collision
        hit=collision(enemyX[i],enemyY[i],bulletX,bulletY) # collision between bullet and enemy
        if hit==True:  # if collision occurs then-
          state=0  # set state ready to fire again
          score_val=score_val+1 # increasing score when bullet hits enemy
          bulletX=playerX+16 # respawning of bullet in x direction
          bulletY=playerY+10 #respawning of bullet in y direction
          enemyX[i]=random.randint(0,736) # respawning of enemy in x direction
          enemyY[i]=0  # respawning of enemy in y direction
          enemy_kill=mixer.Sound('enemy sound.mp3')
          enemy_kill.play()

        # Game over
        if enemyY[i]>=480: # if enemy reaches 480 pixels then game over
            for j in range(0,num): 
                enemyY[j]=600   # all enemy goes to posion 600 (out of screen)
            game_over()  # calling game over function
            break # breaking out of the loop

        enemy(i,enemyX[i],enemyY[i])


        

        

    # Movement of bullet after spacebar is pressed
    if state==1:
        bullet(bulletX,bulletY)
        # no condition for bulletX beacause no bullet movement in x direction
        bulletY=bulletY-bulletY_change # condition for bullet movement in y direction
         
    # Boundary conditions for player
    if playerX<=0:
        playerX=0
    if playerX>=734:
        playerX=734
    if playerY<=0:
        playerY=0
    if playerY>=536:
        playerY=536
    
    # Boundary condition for enemey
    for i in range(0,num):
        if enemyY[i]>=600:
            enemyY[i]=600
    # no boundary condition needed for enemyX coordinate

    # Boundary condition for Bullet
    if bulletY<=0:
        state=0  # bullet ready to fire again
        bulletX=playerX+16 # respawning of bullet in x direction
        bulletY=playerY+10 # respawning of bullet in y direction
    
    player(playerX,playerY) 
    show_score(scoreX,scoreY)
    
    pygame.display.update() # Updating the game screen


