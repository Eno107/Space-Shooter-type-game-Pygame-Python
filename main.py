import pygame
import random
import math

# initialize the pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption(" Bereqet Shooter ")
icon = pygame.image.load("hamburger.png")
pygame.display.set_icon(icon)

# background
bg_image = pygame.image.load("mensa.jpg")
bg_image = pygame.transform.scale(bg_image, (800, 600))
i = 0

# player character
playerIMG = pygame.image.load("pizza.png")
playerX = 370
playerY = 480
k = 0

# Bullet

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_X = 10
text_Y = 10

# game over text
over_font = pygame.font.Font('freesansbold.ttf', 90)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (209, 209, 224))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (209, 209, 224))
    screen.blit(over_text, (100, 150))


# enemy character1
enemyIMG = []
enemyX = []
enemyY = []
enemy_Xchange = []
enemy_Ychange = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyIMG.append(pygame.image.load("chef.png"))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemy_Xchange.append(0.2)
    enemy_Ychange.append(60)


def player(x, y):
    screen.blit(playerIMG, (playerX, playerY))


def enemy(x, y, i):
    screen.blit(enemyIMG[i], (enemyX[i], enemyY[i]))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x, y + 10))


def iscollision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt(math.pow(enemyx - bulletx, 2) + math.pow(enemyy - bullety, 2))
    if distance < 24:
        return True
    else:
        return False


# keeping the game running main function
running = True
while running:
    screen.blit(bg_image, (i, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                k = 0.4
            if event.key == pygame.K_a:
                k = -0.4
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_a:
                k = 0
    playerX += k

    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736

    for i in range(num_of_enemies):
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemy_Xchange[i]
        if enemyX[i] <= 0:
            enemy_Xchange[i] = 0.2
            enemyY[i] += enemy_Ychange[i]
        elif enemyX[i] >= 736:
            enemy_Xchange[i] = -0.2
            enemyY[i] += enemy_Ychange[i]

        # collision
        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

        # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(text_X, text_Y)
    pygame.display.update()

