# Space invaders game development project by Dominators
import pygame
import random

pygame.init()  # initilizing pygame

screen = pygame.display.set_mode((800, 600))  # creating a game window

pygame.display.set_caption("SPACE INVADERS")  # personalizing game window ( Title & Icon
icon = pygame.image.load("Icon.png")
pygame.display.set_icon(icon)

player_img = pygame.image.load('Player.png')  # adding player
playerX = 370
playerY = 480
playerX_change = 0

enemy_img = pygame.image.load('enemy.png')  # adding enemy
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y):
    screen.blit(enemy_img, (x, y))


running = True  # Gamme loop
while running:
    screen.fill((0, 0, 0))  # RGB = Red , Green, Blue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:  # if keystrock is pressed check whether it is right/left
            if event.key == pygame.K_LEFT:
                playerX_change -= 0.1
            if event.key == pygame.K_RIGHT:
                playerX_change += 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

playerX += playerX_change
player(playerX, playerY)
enemy(enemyX, enemyY)
pygame.display.update()  # Call function in running finite loop




