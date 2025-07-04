import pygame
import time
import random

pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Game display
width = 600
height = 400
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game 🐍")

# Clock
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

# Font
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def score_display(score):
    value = score_font.render(f"Score: {score}", True, black)
    dis.blit(value, [0, 0])

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

def game_over_message():
    msg = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, red)
    dis.blit(msg, [width / 6, height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    x_change = 0
    y_change = 0

    snake_list = []
    length = 1

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            dis.fill(white)
            game_over_message()
            score_display(length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        dis.fill(blue)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        score_display(length - 1)
        pygame.display.update()

        if x == foodx and y == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
