import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))

# Título
pygame.display.set_caption("Renado Corre")

# Cores
vermelho = (255, 0, 0)
verde = (0, 255, 0)

# Personagens
renado = pygame.Rect(100, 100, 50, 50)
presente = pygame.Rect(random.randint(0, largura), random.randint(0, altura), 20, 20)
obstaculo = pygame.Rect(random.randint(0, largura), random.randint(0, altura), 30, 30)

# Velocidade
velocidade_renado = 5
velocidade_presente = 2
velocidade_obstaculo = 3

# Pontuação
pontos = 0

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimentação
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP]:
        renado.move_ip(0, -velocidade_renado)
    if teclas[pygame.K_DOWN]:
        renado.move_ip(0, velocidade_renado)
    if teclas[pygame.K_LEFT]:
        renado.move_ip(-velocidade_renado, 0)
    if teclas[pygame.K_RIGHT]:
        renado.move_ip(velocidade_renado, 0)

    # Colisão com presente
    if renado.colliderect(presente):
        pontos += 1
        presente.x = random.randint(0, largura)
        presente.y = random.randint(0, altura)

    # Colisão com obstáculo
    if renado.colliderect(obstaculo):
        pontos -= 1
        obstaculo.x = random.randint(0, largura)
        obstaculo.y = random.randint(0, altura)

    # Atualizar tela
    tela.fill((255, 255, 255))
    pygame.draw.rect(tela, vermelho, renado)
    pygame.draw.rect(tela, verde, presente)
    pygame.draw.rect(tela, (0, 0, 255), obstaculo)
    font = pygame.font.Font(None, 36)
    texto = font.render(f"Pontos: {pontos}", True, (0, 0, 0))
    tela.blit(texto, (10, 10))
    pygame.display.flip()

    # Limitar FPS
    pygame.time.Clock().tick(60)
