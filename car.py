import pygame
import random

pygame.init()

# Screen
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(" Car Dodge Game")

# Load Images
car_img = pygame.image.load("enemy.jfif")
car_img = pygame.transform.scale(car_img, (50, 80))

obs_img = pygame.image.load("my.jfif")
obs_img = pygame.transform.scale(obs_img, (50, 80))

# Car
car_width, car_height = 50, 80
car_x = width // 2
car_y = height - 100
car_speed = 6

# Obstacle
obs_width, obs_height = 50, 80
obs_x = random.randint(0, width - obs_width)
obs_y = -100
obs_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 35)

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= car_speed
    if keys[pygame.K_RIGHT]:
        car_x += car_speed

    car_x = max(0, min(width - car_width, car_x))

    # Move obstacle
    obs_y += obs_speed

    if obs_y > height:
        obs_y = -100
        obs_x = random.randint(0, width - obs_width)
        score += 1

    # Collision
    if (
        car_x < obs_x + obs_width and
        car_x + car_width > obs_x and
        car_y < obs_y + obs_height and
        car_y + car_height > obs_y
    ):
        print(" Game Over! Score:", score)
        running = False

    # Draw
    screen.fill((50, 50, 50))  # road color

    # Draw images instead of rectangles
    screen.blit(car_img, (car_x, car_y))
    screen.blit(obs_img, (obs_x, obs_y))

    # Score
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.update()

pygame.quit()