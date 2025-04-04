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
mode = "brush"  # Режимы: brush, rect, circle, eraser, square, right_triangle, equilateral_triangle, rhombus

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
            if clear_button.collidepoint(event.pos):  # Очистка экрана при клике на кнопку
                screen.fill(WHITE)
            else:
                drawing = True
                start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = pygame.mouse.get_pos()
            if mode == "rect":
                pygame.draw.rect(screen, current_color, pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])), 2)
            elif mode == "circle":
                radius = int(((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)**0.5)
                pygame.draw.circle(screen, current_color, start_pos, radius, 2)
            elif mode == "square":
                side = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                pygame.draw.rect(screen, current_color, pygame.Rect(start_pos, (side, side)), 2)
            elif mode == "right_triangle":
                points = [start_pos, (end_pos[0], start_pos[1]), end_pos]
                pygame.draw.polygon(screen, current_color, points, 2)
            elif mode == "equilateral_triangle":
                side = abs(end_pos[0] - start_pos[0])
                height = int(side * (3 ** 0.5) / 2)
                points = [start_pos, (start_pos[0] + side, start_pos[1]), (start_pos[0] + side // 2, start_pos[1] - height)]
                pygame.draw.polygon(screen, current_color, points, 2)
            elif mode == "rhombus":
                mid_x = (start_pos[0] + end_pos[0]) // 2
                mid_y = (start_pos[1] + end_pos[1]) // 2
                points = [(mid_x, start_pos[1]), (end_pos[0], mid_y), (mid_x, end_pos[1]), (start_pos[0], mid_y)]
                pygame.draw.polygon(screen, current_color, points, 2)
        elif event.type == pygame.MOUSEMOTION and drawing:
            if mode == "brush":
                pygame.draw.circle(screen, current_color, event.pos, brush_size)  # Рисование кистью
            elif mode == "eraser":
                pygame.draw.circle(screen, WHITE, event.pos, brush_size)  # Стирание
        elif event.type == pygame.KEYDOWN:
            # Переключение режимов и цветов
            if event.key == pygame.K_b:  # Кисть
                mode = "brush"
            elif event.key == pygame.K_r:  # Прямоугольник
                mode = "rect"
            elif event.key == pygame.K_c:  # Круг
                mode = "circle"
            elif event.key == pygame.K_e:  # Ластик
                mode = "eraser"
            elif event.key == pygame.K_s:  # Квадрат
                mode = "square"
            elif event.key == pygame.K_t:  # Прямоугольный треугольник
                mode = "right_triangle"
            elif event.key == pygame.K_y:  # Равносторонний треугольник
                mode = "equilateral_triangle"
            elif event.key == pygame.K_u:  # Ромб
                mode = "rhombus"
            elif event.key == pygame.K_1:  # Черный
                current_color = BLACK
            elif event.key == pygame.K_2:  # Красный
                current_color = RED
            elif event.key == pygame.K_3:  # Зеленый
                current_color = GREEN
            elif event.key == pygame.K_4:  # Синий
                current_color = BLUE

    # Отрисовка кнопки "Clear"
    pygame.draw.rect(screen, BLACK, clear_button, 2)
    clear_text = font.render("Clear", True, BLACK)
    screen.blit(clear_text, (710, 15))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()