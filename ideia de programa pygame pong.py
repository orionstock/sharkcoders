import pygame
import sys

pygame.init()
pygame.mixer.init()

som_bounce = pygame.mixer.Sound("pingpongboard.ogg")

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pong")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 74)

left_barra = pygame.Rect(30, 250, 15, 100)
right_barra = pygame.Rect(755, 250, 15, 100)

bola = pygame.Rect(390, 290, 20, 20)
bola_speed_x = 5
bola_speed_y = 5

left_score = 0
right_score = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()


    if keys[pygame.K_w]:
        left_barra.y -= 6
    if keys[pygame.K_s]:
        left_barra.y += 6

    if keys[pygame.K_UP]:
        right_barra.y -= 6
    if keys[pygame.K_DOWN]:
        right_barra.y += 6


    left_barra.clamp_ip(screen.get_rect())
    right_barra.clamp_ip(screen.get_rect())

    bola.x += bola_speed_x
    bola.y += bola_speed_y

    if bola.top <= 0 or bola.bottom >= HEIGHT:
        bola_speed_y *= -1

    if bola.colliderect(left_barra) or bola.colliderect(right_barra):
        bola_speed_x *= -1
        som_bounce.play()

    if bola.left <= 0:
        right_score += 1
        bola.center = (WIDTH // 2, HEIGHT // 2)

    if bola.right >= WIDTH:
        left_score += 1
        bola.center = (WIDTH // 2, HEIGHT // 2)



    screen.fill((0, 0, 0, 30))

    pygame.draw.rect(screen, (255, 255, 255), left_barra)
    pygame.draw.rect(screen, (255, 255, 255), right_barra)
    pygame.draw.ellipse(screen, (255, 255, 255), bola)

    pygame.draw.aaline(
        screen,(255, 255, 255), (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))


    left_text = font.render(str(left_score), True, (255, 255, 255))
    right_text = font.render(str(right_score), True, (255, 255, 255))


    screen.blit(left_text, (250, 20))
    screen.blit(right_text, (500, 20))


    pygame.display.flip()
    clock.tick(60)



