import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Racer")
clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Загружаем изображения
road_img = pygame.image.load("AnimatedStreet.png").convert()
road_img = pygame.transform.scale(road_img, (800, 600))
player1_img = pygame.image.load("Player.png").convert_alpha()  # Машина первого игрока
player1_img = pygame.transform.scale(player1_img, (50, 100))
player2_img = pygame.image.load("Enemy.png").convert_alpha()  # Машина второго игрока
player2_img = pygame.transform.scale(player2_img, (50, 100))
coin_img = pygame.image.load("coin.png").convert_alpha()
coin_img = pygame.transform.scale(coin_img, (30, 30))

# Параметры первого игрока
player1_rect = player1_img.get_rect(center=(400, 500))
player1_speed = 5
player1_coins = 0

# Параметры второго игрока (врага)
player2_rect = player2_img.get_rect(center=(300, 500))
player2_speed = 5  # Начальная скорость второго игрока
player2_coins = 0

# Параметры монет
coins = []
coin_spawn_timer = 0
coin_spawn_rate = 60  # Частота появления монет (каждые 60 кадров)
coin_weights = [1, 5, 10]  # Разные веса монет

# Шрифт для счётчиков монет
font = pygame.font.SysFont("Arial", 30)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление первым игроком (стрелки)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player1_rect.left > 2:
        player1_rect.x -= player1_speed
    if keys[pygame.K_RIGHT] and player1_rect.right < 798:
        player1_rect.x += player1_speed
    if keys[pygame.K_UP] and player1_rect.top > 2:
        player1_rect.y -= player1_speed
    if keys[pygame.K_DOWN] and player1_rect.bottom < 598:
        player1_rect.y += player1_speed

    # Управление вторым игроком (WASD)
    if keys[pygame.K_a] and player2_rect.left > 2:
        player2_rect.x -= player2_speed
    if keys[pygame.K_d] and player2_rect.right < 798:
        player2_rect.x += player2_speed
    if keys[pygame.K_w] and player2_rect.top > 2:
        player2_rect.y -= player2_speed
    if keys[pygame.K_s] and player2_rect.bottom < 598:
        player2_rect.y += player2_speed

    # Спавн монет с разными весами
    coin_spawn_timer += 1
    if coin_spawn_timer >= coin_spawn_rate:
        coin_pos = [random.randint(0, 770), random.randint(0, 570)]
        weight = random.choice(coin_weights)  # Случайный вес монеты
        coins.append({"rect": pygame.Rect(coin_pos[0], coin_pos[1], 30, 30), "weight": weight})
        coin_spawn_timer = 0

    # Проверка столкновений с монетами
    for coin in coins[:]:
        if player1_rect.colliderect(coin["rect"]):
            coins.remove(coin)
            player1_coins += coin["weight"]  # Увеличиваем счет игрока 1 на вес монеты
        elif player2_rect.colliderect(coin["rect"]):
            coins.remove(coin)
            player2_coins += coin["weight"]  # Увеличиваем счет игрока 2 на вес монеты

    # Увеличение скорости второго игрока после каждых 10 монет у первого игрока
    if player1_coins >= 10 and player1_coins % 10 == 0:
        player2_speed += 1  # Увеличиваем скорость второго игрока

    # Отрисовка
    screen.blit(road_img, (0, 0))  # Отрисовка дороги как фона
    screen.blit(player1_img, player1_rect)  # Отрисовка первого игрока
    screen.blit(player2_img, player2_rect)  # Отрисовка второго игрока
    for coin in coins:
        screen.blit(coin_img, coin["rect"])  # Отрисовка монет

    # Отображение счётчиков монет
    player1_text = font.render(f"P1 Coins: {player1_coins}", True, BLACK)
    screen.blit(player1_text, (650, 10))  # Счетчик первого игрока
    player2_text = font.render(f"P2 Coins: {player2_coins}", True, BLACK)
    screen.blit(player2_text, (10, 10))  # Счетчик второго игрока

    pygame.display.flip()
    clock.tick(60)

pygame.quit() 