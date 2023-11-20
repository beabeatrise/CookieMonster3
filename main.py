import pygame
import random
import math

# this is main.py file

pygame.init()

screen = pygame.display.set_mode((700, 500)) 
pygame.display.set_caption('Cookie Monster: catch the cookies with cursor control keys!')
icon = pygame.image.load('monster.png')
pygame.display.set_icon(icon)
background = pygame.image.load('underground.png')

monsterImg = pygame.image.load('monster.png')
monsterX = 350
monsterY = 250

cookieImg = pygame.image.load('cookie.png')
cookieX = random.randint(0, 664)
cookieY = random.randint(0, 464)

monsterX_change = 0
monsterY_change = 0

score = 0
font = pygame.font.SysFont('comicsansms', 32)

def show_monster(x, y):
    screen.blit(monsterImg, (x, y))

def show_cookie(x, y):
    screen.blit(cookieImg, (x, y))

def show_score(score):
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

def is_cookie_eaten(mX, mY, cX, cY):
    distance = math.sqrt(math.pow((mX+64/2) - (cX+32/2), 2) + (math.pow((mY+32) - (cY+16), 2)))
    if distance <= 48:
        return True

while True:
    screen.fill((0, 0, 0)) 
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                monsterX_change = -0.5
                monsterY_change = 0
            if event.key == pygame.K_RIGHT:
                monsterX_change = 0.5
                monsterY_change = 0
            if event.key == pygame.K_UP:
                monsterX_change = 0
                monsterY_change = -0.5
            if event.key == pygame.K_DOWN:
                monsterX_change = 0
                monsterY_change = 0.5
       

    monsterX += monsterX_change
    monsterY += monsterY_change

    if monsterX <= 0:
        monsterX = 0
    if monsterY <= 0:
        monsterY = 0
    if monsterX >= 636:
        monsterX = 636
    if monsterY >= 436:
        monsterY = 436

    if is_cookie_eaten(monsterX, monsterY, cookieX, cookieY) == True:
        cookieX = random.randint(0, 664)
        cookieY = random.randint(0, 464)
        score = score + 1


    show_monster(monsterX, monsterY)
    show_cookie(cookieX, cookieY)
    show_score(score)
    pygame.display.update()