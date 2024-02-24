import pygame
import time
import random

WIDTH, HEIGHT = 800, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie Fighter")

#////////////////////////// BACKGROUND ///////////////////////////

BG = pygame.transform.scale(pygame.image.load("7682-v2.jpg"), (WIDTH, HEIGHT))

#////////////////////////// BACKGROUND ///////////////////////////

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5

#//////////////////////////// PLAYER /////////////////////////////

def draw(player):

    WIN.blit(BG, (  (0, 0)))

    pygame.draw.rect(WIN, "red", player)

    pygame.display.update()

#//////////////////////////// PLAYER /////////////////////////////

#///////////////////////////// MAIN //////////////////////////////

def main():

    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    
    while run:

        clock.tick(60)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                run = False 
                break

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:

            player.x -= PLAYER_VEL
        
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:

            player.x += PLAYER_VEL

        draw(player)

    pygame.quit()

#///////////////////////////// MAIN //////////////////////////////

if __name__ == "__main__":

    main()
