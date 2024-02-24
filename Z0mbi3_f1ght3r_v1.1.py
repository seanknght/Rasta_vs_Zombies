import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 700
PLAYER_SIZE = 50
ZOMBIE_SIZE = 50
BULLET_SIZE = 10
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie Shooter")

# Load background image
background_image = pygame.image.load("7682-v2.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Load images
player_image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
player_image.fill(RED)

zombie_image = pygame.Surface((ZOMBIE_SIZE, ZOMBIE_SIZE))
zombie_image.fill(GREEN)

bullet_image = pygame.Surface((BULLET_SIZE, BULLET_SIZE))
bullet_image.fill(WHITE)

# Game variables
player = pygame.Rect(WIDTH // 2 - PLAYER_SIZE // 2, HEIGHT - PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)
zombies = []
bullets = []

clock = pygame.time.Clock()

def spawn_zombie():
    zombie = pygame.Rect(random.randint(0, WIDTH - ZOMBIE_SIZE), 0, ZOMBIE_SIZE, ZOMBIE_SIZE)
    zombies.append(zombie)

def draw_window(game_over=False):
    # Draw background
    screen.blit(background_image, (0, 0))

    if not game_over:
        # Draw player
        pygame.draw.rect(screen, RED, player)

        # Draw zombies
        for zombie in zombies:
            pygame.draw.rect(screen, GREEN, zombie)

        # Draw bullets
        for bullet in bullets:
            pygame.draw.rect(screen, WHITE, bullet)
    else:
        # Display "Game Over" text
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, (255, 0, 0))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

        # Display "Press R to Restart" text
        font = pygame.font.Font(None, 36)
        restart_text = font.render("Press R to Restart", True, (255, 255, 255))
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 50))

    pygame.display.flip()

# Main game loop
bullet_fired = False  # Variable to track whether a bullet has been fired
game_over = False

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                # Restart the game
                player = pygame.Rect(WIDTH // 2 - PLAYER_SIZE // 2, HEIGHT - PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)
                zombies = []
                bullets = []
                game_over = False

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - 5 > 0:
            player.x -= 5 
        if keys[pygame.K_RIGHT] and player.x + 5 < WIDTH - PLAYER_SIZE:
            player.x += 5

        # Spawn zombies randomly
        if random.randint(0, 500) < 5:
            spawn_zombie()

        # Move and update zombies
        for zombie in zombies:
            zombie.y += 5
            if zombie.colliderect(player):
                game_over = True

        # Move and update bullets
        bullets = [bullet for bullet in bullets if bullet.y > 0]
        for bullet in bullets:
            bullet.y -= 10

            # Check for collisions with zombies
            for zombie in zombies:
                if bullet.colliderect(zombie):
                    zombies.remove(zombie)
                    bullets.remove(bullet)
                    break  # Exit the inner loop after hitting a zombie

        # Check for shooting (allow firing only if a bullet hasn't been fired)
        if keys[pygame.K_SPACE] and not bullet_fired:
            bullet = pygame.Rect(player.x + PLAYER_SIZE // 2 - BULLET_SIZE // 2, player.y, BULLET_SIZE, BULLET_SIZE)
            bullets.append(bullet)
            bullet_fired = True  # Set the flag to indicate that a bullet has been fired

        # Reset the bullet_fired flag when the spacebar is released
        if not keys[pygame.K_SPACE]:
            bullet_fired = False

    draw_window(game_over)
