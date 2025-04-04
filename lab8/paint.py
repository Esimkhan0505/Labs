import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
colors = [BLACK, RED, GREEN, BLUE]
current_color = BLACK
brush_size = 10
mode = "brush"  # brush, rect, circle, eraser

# Очистка экрана в начале
screen.fill(WHITE)
drawing = False

# Шрифт для кнопки
font = pygame.font.SysFont("Arial", 20)
clear_button = pygame.Rect(700, 10, 80, 30)  # Прямоугольник кнопки "Clear"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if clear_button.collidepoint(event.pos):  # Проверка клика по кнопке
                screen.fill(WHITE)  # Очищаем экран
            else:
                drawing = True
                start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            if mode == "rect":
                pygame.draw.rect(screen, current_color, pygame.Rect(start_pos, (pygame.mouse.get_pos()[0] - start_pos[0], pygame.mouse.get_pos()[1] - start_pos[1])), 2)
            elif mode == "circle":
                radius = int(((pygame.mouse.get_pos()[0] - start_pos[0])**2 + (pygame.mouse.get_pos()[1] - start_pos[1])**2)**0.5)
                pygame.draw.circle(screen, current_color, start_pos, radius, 2)
        elif event.type == pygame.MOUSEMOTION and drawing:
            if mode == "brush":
                pygame.draw.circle(screen, current_color, event.pos, brush_size)
            elif mode == "eraser":
                pygame.draw.circle(screen, WHITE, event.pos, brush_size)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:  # Brush
                mode = "brush"
            elif event.key == pygame.K_r:  # Rectangle
                mode = "rect"
            elif event.key == pygame.K_c:  # Circle
                mode = "circle"
            elif event.key == pygame.K_e:  # Eraser
                mode = "eraser"
            elif event.key == pygame.K_1:  # Черный
                current_color = BLACK
            elif event.key == pygame.K_2:  # Красный
                current_color = RED
            elif event.key == pygame.K_3:  # Зелёный
                current_color = GREEN
            elif event.key == pygame.K_4:  # Синий
                current_color = BLUE

    # Отрисовка кнопки "Clear"
    pygame.draw.rect(screen, BLACK, clear_button, 2)  # Рамка кнопки
    clear_text = font.render("Clear", True, BLACK)
    screen.blit(clear_text, (710, 15))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()