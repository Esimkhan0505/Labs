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
snake_list = [[300, 200]]  # Начальная позиция змейки
snake_direction = "RIGHT"
food = {"pos": [random.randrange(0, 600, snake_block), random.randrange(0, 400, snake_block)], 
        "weight": random.choice([10, 20, 30]), "timer": 300}  # Еда с весом и таймером (300 кадров ~ 5 сек)
score = 0
level = 1
food_count = 0

# Шрифт для счётчиков
font = pygame.font.SysFont("Arial", 25)

def generate_food():
    # Генерация новой еды с проверкой, чтобы она не появлялась на змейке
    while True:
        pos = [random.randrange(0, 600, snake_block), random.randrange(0, 400, snake_block)]
        if pos not in snake_list:
            return {"pos": pos, "weight": random.choice([10, 20, 30]), "timer": 300}

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Управление направлением змейки
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
    if head == food["pos"]:
        score += food["weight"]  # Увеличиваем счет на вес еды
        food_count += 1
        food = generate_food()  # Генерируем новую еду
        if food_count >= 3:  # Новый уровень каждые 3 еды
            level += 1
            snake_speed += 5  # Увеличиваем скорость
            food_count = 0
    else:
        snake_list.pop(0)  # Удаляем хвост, если еды нет

    # Таймер исчезновения еды
    food["timer"] -= 1
    if food["timer"] <= 0:
        food = generate_food()  # Если таймер истек, генерируем новую еду

    # Отрисовка
    screen.fill(WHITE)
    for pos in snake_list:
        pygame.draw.rect(screen, GREEN, [pos[0], pos[1], snake_block, snake_block])  # Отрисовка змейки
    pygame.draw.rect(screen, RED, [food["pos"][0], food["pos"][1], snake_block, snake_block])  # Отрисовка еды

    # Отображение счёта и уровня
    score_text = font.render(f"Score: {score}", True, BLACK)
    level_text = font.render(f"Level: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.flip()
    clock.tick(snake_speed)

pygame.quit()