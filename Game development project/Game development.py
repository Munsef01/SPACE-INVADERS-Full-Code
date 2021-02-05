# Space invaders game development project by Dominators
import pygame
import random
import math
from pygame import mixer

pygame.init()  # initilizing pygame

screen = pygame.display.set_mode((800, 600))  # creating a game window

background = pygame.image.load("Background.png")  # adding background image


#Background Sounds

mixer.music.load("backgroundMusic.mp3")
mixer.music.play(-1)

pygame.display.set_caption("SPACE INVADERS")  # personalizing game window ( Title & Icon
icon = pygame.image.load("Icon.png")
pygame.display.set_icon(icon)

player_img = pygame.image.load('Player.png')  # adding player
playerX = 370
playerY = 480
playerX_change = 0


enemy_img = []                 # Adding enemy
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

num_of_enymies = 6

for i in range (num_of_enymies):

    enemy_img.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append (4)
    enemyY_change.append(10)

bullet_img = pygame.image.load('bullet.png')  # adding bullet
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 15
bullet_state = ("ready")

score_value = 0                                   #score
font = pygame.font.Font("freesansbold.ttf", 32)

textX =  10
textY = 10

# Game Over Text

over_font = pygame.font.Font("freesansbold.ttf", 64)

def show_score(x,y):
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render(" GAME OVER ", True, (255, 0, 0))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_img[i], (x , y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulleX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulleX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

running = True  # Gamme loop
while running:
    screen.fill((0, 0, 0))  # RGB = Red , Green, Blue

    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:  # if keystrock is pressed check whether it is right/left
            if event.key == pygame.K_LEFT:
                playerX_change -= 5
            if event.key == pygame.K_RIGHT:
                playerX_change += 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":     # Get the current x cordinate of the spaceship
                    bullet_Sound = mixer.Sound("BulletShoot.wav")
                    bullet_Sound.play()
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change  # checking for boundaries of spaceships, so it wont go out of bounds...

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736


    for i in range( num_of_enymies):          # enemy movement

        # Game Over
        if enemyY [i] > 400:
           for j in range(num_of_enymies):
               enemyY[j] = 2000
           game_over_text()
           break

        enemyX [i] += enemyX_change [i]
        if enemyX [i] <= 0:
            enemyX_change [i] = 4
            enemyY [i] += enemyY_change [i]
        elif enemyX [i] >= 736:
            enemyX_change [i] = -4
            enemyY [i] += enemyY_change [i]

        collission = isCollision(enemyX [i] , enemyY [i], bulletX, bulletY)  # Colllision
        if collission:
            explosion_Sound = mixer.Sound("EnemyCrashes.wav")
            explosion_Sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX [i] = random.randint(0, 735)
            enemyY [i] = random.randint(50, 150)
        enemy(enemyX[i] , enemyY[i],i)

    if bulletY <= 0 :
         bulletY = 480
         bullet_state = "ready"
    if bullet_state is "fire":          # bullet Movement
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change



    player(playerX, playerY)
    show_score(textX,textY)
    pygame.display.update()  # Call function in running finite loop
