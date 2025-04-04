import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Параметры змейки
snake_block = 20
snake_speed = 15  # Начальная скорость 
snake_list = [[300, 200]]  # Начальная позиция
snake_direction = "RIGHT"
food_pos = [random.randrange(0, 600, snake_block), random.randrange(0, 400, snake_block)]
score = 0
level = 1
food_count = 0

# Шрифт для счётчиков
font = pygame.font.SysFont("Arial", 25)

def generate_food():
    while True:
        pos = [random.randrange(0, 600, snake_block), random.randrange(0, 400, snake_block)]
        if pos not in snake_list:  # Проверяем, что еда не на змейке
            return pos

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"
            elif event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"

    # Движение змейки
    head = snake_list[-1].copy()
    if snake_direction == "LEFT":
        head[0] -= snake_block
    elif snake_direction == "RIGHT":
        head[0] += snake_block
    elif snake_direction == "UP":
        head[1] -= snake_block
    elif snake_direction == "DOWN":
        head[1] += snake_block

    # Проверка столкновения с границами
    if head[0] < 0 or head[0] >= 600 or head[1] < 0 or head[1] >= 400:
        running = False  # Игра заканчивается при выходе за границы

    snake_list.append(head)

    # Проверка столкновения с едой
    if head == food_pos:
        score += 10
        food_count += 1
        food_pos = generate_food()
        if food_count >= 3:  # Новый уровень каждые 3 еды
            level += 1
            snake_speed += 5  # Увеличиваем скорость
            food_count = 0
    else:
        snake_list.pop(0)  # Удаляем хвост, если еды нет

    # Отрисовка
    screen.fill(WHITE)
    for pos in snake_list:
        pygame.draw.rect(screen, GREEN, [pos[0], pos[1], snake_block, snake_block])
    pygame.draw.rect(screen, RED, [food_pos[0], food_pos[1], snake_block, snake_block])

    # Отображение счёта и уровня
    score_text = font.render(f"Score: {score}", True, BLACK)
    level_text = font.render(f"Level: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.flip()
    clock.tick(snake_speed)

pygame.quit()