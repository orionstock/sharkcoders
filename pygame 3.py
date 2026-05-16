import pygame

pygame.init()

LARGURA = 640
ALTURA = 480

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Círculo Controlado")

fundo = (30, 30, 30)
running = True

verde = (0, 255, 0)
vermelho = (255, 0, 0)

cor_atual = verde


def trocar_cor(cor):
    if cor == verde:
        return vermelho
    else: return verde

x = LARGURA // 2
y = ALTURA // 2

tamanho = 50

velocidade = 1

while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= velocidade

    if keys[pygame.K_RIGHT]:
        x += velocidade

    if keys[pygame.K_UP]:
        y -= velocidade

    if keys[pygame.K_DOWN]:
        y += velocidade

    if keys[pygame.K_SPACE]:
        cor_atual = trocar_cor(cor_atual)


    if x < 0:
        x = 0

    if x > LARGURA - tamanho:
        x = LARGURA - tamanho

    if y < 0:
        y = 0

    if y > ALTURA - tamanho:
        y = ALTURA - tamanho

    tela.fill(fundo)
    pygame.draw.circle(tela, cor_atual, (x, y), 20)
    pygame.display.flip()



pygame.quit()