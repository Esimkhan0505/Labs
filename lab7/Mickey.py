import pygame
import time
import math

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Mickey Clock")
clock = pygame.time.Clock()

mickey_image = pygame.image.load("clock.png").convert_alpha()
min_hand = pygame.image.load("min_hand.png").convert_alpha()
sec_hand = pygame.image.load("sec_hand.png").convert_alpha()

mickey_image = pygame.transform.scale(mickey_image, (200, 200))
min_hand = pygame.transform.scale(min_hand, (280, 120))  
sec_hand = pygame.transform.scale(sec_hand, (300, 150))  

mickey_rect = mickey_image.get_rect(center=(200, 200))


font = pygame.font.SysFont("Arial", 30)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

   
    minute_angle = -(minutes * 6 - 90) 
    second_angle = -(seconds * 6 - 90)  

   
    rotated_min_hand = pygame.transform.rotate(min_hand, minute_angle)
    rotated_sec_hand = pygame.transform.rotate(sec_hand, second_angle)

  
    min_hand_rect = rotated_min_hand.get_rect(center=(200, 200))
    sec_hand_rect = rotated_sec_hand.get_rect(center=(200, 200))

   
    time_str = f"{minutes:02d}:{seconds:02d}"
    time_text = font.render(time_str, True, (0, 0, 0))

    screen.fill((255, 255, 255))
    screen.blit(mickey_image, mickey_rect)
    screen.blit(rotated_min_hand, min_hand_rect)
    screen.blit(rotated_sec_hand, sec_hand_rect)
    screen.blit(time_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()