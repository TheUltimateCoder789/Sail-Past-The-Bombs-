import random
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Sail Past The Bombs")
clock = pygame.time.Clock()

background = pygame.image.load('Graphics/Ocean.png')
background_width = background.get_width()
background_x = 0

ship = pygame.image.load('Graphics/Ship.png')
ship_width = 150
ship_height = 171
ship_x = 400
ship_y = 500 - ship_height // 2

shiprect = pygame.Rect(ship_x, ship_y, ship_width, ship_height)

bomb = pygame.image.load("Graphics/BombIcon.png")
bomb_width = 100
bomb_height = 94
bomb_x = 1000
bomb_y = random.randint(310, 530)
bombrect = pygame.Rect(bomb_x, bomb_y, bomb_width, bomb_height)
bomb_speed = 6

font = pygame.font.Font(None, 36)

background_speed = 2
background_speed_increment = 0.5 
count = 0;

paused = False  # Game pause state

def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if not paused:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if shiprect.bottom >= 410:
                    shiprect.centery -= 6
            if event.key == pygame.K_DOWN:
                if shiprect.bottom <= 605:
                    shiprect.centery += 6

        counter_text = font.render("Time: " + str(count), True, (255, 255, 255))

        screen.blit(background, (background_x, 0))
        screen.blit(background, (background_x + background_width, 0))
        background_x -= background_speed

        if background_x <= -background_width:
            background_x = 0
            background_speed += background_speed_increment

        bombrect.left -= bomb_speed

        if bombrect.right <= 0:
            bombrect.left = 1000
            bombrect.top = random.randint(310, 530)
            bomb_speed += 0.3  # Bomb speed increment

        if check_collision(shiprect, bombrect) and (bombrect.y >= shiprect.y + 10 and bombrect.y <= shiprect.y + 115) and (bombrect.x <= shiprect.x + 115 and bombrect.x >= shiprect.x - 50):
            paused = True
            print("Collision occurred! Game Over.")

        screen.blit(bomb, bombrect)
        screen.blit(ship, shiprect)
    count = count + 1
    screen.blit(counter_text, (10, 10))
    pygame.display.update()
    clock.tick(60)
