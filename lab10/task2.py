import pygame
import random
import psycopg2


conn = psycopg2.connect(
    host="localhost",
    dbname="Lab works",
    user="postgres",
    password="Qwertyeska12"
)
cur = conn.cursor()


username = input("Enter your username: ")


cur.execute("SELECT id FROM users WHERE username = %s", (username,))
user = cur.fetchone()
if user:
    user_id = user[0]
    cur.execute("SELECT MAX(level), MAX(score) FROM user_score WHERE user_id = %s", (user_id,))
    lvl, scr = cur.fetchone()
    print(f"Welcome back, {username}! Last level: {lvl}, score: {scr}")
else:
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    conn.commit()
    print(f"Welcome, {username}!")


pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

WHITE = (200, 200, 200)  
GREEN = (0, 255, 0)     
YELLOW = (255, 255, 0)   
RED = (255, 0, 0)       
BLACK = (0, 0, 0)

snake_block, snake_speed = 20, 15
snake_list = [[300, 200]]
snake_direction = "RIGHT"
food_pos = [random.randrange(0, 600, snake_block), random.randrange(0, 400, snake_block)]
score, level, food_count = 0, 1, 0
font = pygame.font.SysFont("Arial", 25)

def generate_food():
    while True:
        pos = [random.randrange(0, 600, snake_block), random.randrange(0, 400, snake_block)]
        if pos not in snake_list:
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
            elif event.key == pygame.K_ESCAPE:
                running = False  # Выход по ESC

    head = snake_list[-1].copy()
    if snake_direction == "LEFT":
        head[0] -= snake_block
    elif snake_direction == "RIGHT":
        head[0] += snake_block
    elif snake_direction == "UP":
        head[1] -= snake_block
    elif snake_direction == "DOWN":
        head[1] += snake_block

 
    if head[0] < 0:
        head[0] = 600 - snake_block
    elif head[0] >= 600:
        head[0] = 0
    elif head[1] < 0:
        head[1] = 400 - snake_block
    elif head[1] >= 400:
        head[1] = 0
        
    if head in snake_list:
        running = False  
    


    snake_list.append(head)

    if head == food_pos:
        score += 10
        food_count += 1
        food_pos = generate_food()
        if food_count >= 3:
            level += 1
            snake_speed += 5
            food_count = 0
    else:
        snake_list.pop(0)

    screen.fill(WHITE)
    for pos in snake_list:
        pygame.draw.rect(screen, GREEN, [pos[0], pos[1], snake_block, snake_block])
    pygame.draw.rect(screen, RED, [food_pos[0], food_pos[1], snake_block, snake_block])

    screen.blit(font.render(f"Score: {score}", True, BLACK), (10, 10))
    screen.blit(font.render(f"Level: {level}", True, BLACK), (10, 40))

    pygame.display.flip()
    clock.tick(snake_speed)

pygame.quit()


cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)",
            (user_id, score, level))
conn.commit()
cur.close()
conn.close()
print(f"Game over! Your score: {score}, level: {level}")
