import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Red Ball")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 0, 0)


ball_x, ball_y = 200, 200
ball_radius = 25
move_speed = 20

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_y - ball_radius - move_speed >= 0:
                ball_y -= move_speed
            elif event.key == pygame.K_DOWN and ball_y + ball_radius + move_speed <= 400:
                ball_y += move_speed
            elif event.key == pygame.K_LEFT and ball_x - ball_radius - move_speed >= 0:
                ball_x -= move_speed
            elif event.key == pygame.K_RIGHT and ball_x + ball_radius + move_speed <= 400:
                ball_x += move_speed

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()