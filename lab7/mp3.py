import pygame

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")
clock = pygame.time.Clock()

music_files = ["Don Toliver - No Pole.mp3", "Travis-Scott-FE-N-.mp3",  "Steve Lacy - Dark Red.mp3"]
current_track = 0

pygame.mixer.music.load(music_files[current_track])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pygame.mixer.music.play()
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_n:
                current_track = (current_track + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play()
            elif event.key == pygame.K_b:
                current_track = (current_track - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play()

    screen.fill((255, 255, 255))
    font = pygame.font.SysFont("Arial", 20)
    text = font.render(f"Playing: {music_files[current_track]}", True, (0, 0, 0))
    screen.blit(text, (10, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()