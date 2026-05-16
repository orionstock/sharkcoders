import pygame

pygame.init()
tela = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Janela Pygame Fixolas")

fundo = (30, 30, 30)
running = True

while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    tela.fill(fundo)
    pygame.draw.rect(tela, (255, 0, 0), (50, 50, 100, 80))
    pygame.draw.circle(tela, (0, 255, 0), (320, 240), 40)
    pygame.draw.line(tela, (0, 0, 255), (0, 0), (640, 480), 3)
    pygame.display.flip()


pygame.quit()
