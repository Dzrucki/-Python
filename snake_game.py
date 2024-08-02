import pygame
import time
import random
from snake import Snake
from food import Food

# Инициализация pygame
pygame.init()

# Определение цветов
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Размеры экрана
dis_width = 800
dis_height = 600

# Создание экрана
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
snake_speed = 15

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    game_over = False
    game_close = False

    snake = Snake(dis_width / 2, dis_height / 2)
    food = Food(dis_width, dis_height, snake.block_size)

    while not game_over:
        while game_close:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
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
                    snake.change_direction('LEFT')
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction('RIGHT')
                elif event.key == pygame.K_UP:
                    snake.change_direction('UP')
                elif event.key == pygame.K_DOWN:
                    snake.change_direction('DOWN')

        if snake.has_collided(dis_width, dis_height):
            game_close = True

        snake.move()
        dis.fill(blue)
        food.draw(dis)
        snake.draw(dis)

        pygame.display.update()

        if snake.eat(food.x, food.y):
            food = Food(dis_width, dis_height, snake.block_size)
            snake.grow()

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
