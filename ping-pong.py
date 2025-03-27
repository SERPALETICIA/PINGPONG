import sys
import pygame
import random


VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

largura= 800
altura= 600

screen= pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pong")

raquete_largura = 10
raquete_altura = 60
tamanho_bola = 10

pc_x = 10
pc_y = altura // 2 - raquete_altura // 2

player_1_x = largura - 20 
player_1_y = altura // 2 - raquete_altura // 2

bola_x = largura // 2 - tamanho_bola // 2 
bola_y = altura // 2 - tamanho_bola // 2 

raquete_player_1_dy = 5
raquete_pc_dy = 5
velocidade_bola_x = 5
velocidade_bola_y = 5

clock = pygame.time.Clock()


rodando = True

def cor_aleatoria():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

bola_cor = BRANCO 

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False 
    
    screen.fill(PRETO)

    bola_x += velocidade_bola_x
    bola_y += velocidade_bola_y

    if bola_y <= 0 or bola_y >= altura - tamanho_bola:
        velocidade_bola_y = -velocidade_bola_y
        bola_cor = cor_aleatoria()
      
    if bola_x <= 0 or bola_x >= largura - tamanho_bola:
        bola_x = largura // 2 - tamanho_bola // 2 
        bola_y = altura // 2 - tamanho_bola // 2
        bola_cor = cor_aleatoria() 
        
    if pc_y + raquete_altura / 2 < bola_y:
        pc_y += raquete_pc_dy
    elif pc_y + raquete_altura / 2 > bola_y:
        pc_y -= raquete_pc_dy

    if pc_y <= 0:
        pc_y = 0
    elif pc_y >= altura - raquete_altura:
        pc_y = altura - raquete_altura

    bola_rect = pygame.Rect(bola_x, bola_y, tamanho_bola, tamanho_bola)

    if bola_rect.colliderect(
        pygame.Rect(player_1_x, player_1_y, raquete_largura, raquete_altura)
    ):
        velocidade_bola_x = -velocidade_bola_x
        bola_cor = cor_aleatoria()
    
    if bola_rect.colliderect(
        pygame.Rect(pc_x, pc_y, raquete_largura, raquete_altura)
    ):
        velocidade_bola_x = -velocidade_bola_x
        bola_cor = cor_aleatoria()
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and player_1_y > 0:
        player_1_y -= raquete_player_1_dy
    if keys[pygame.K_DOWN] and player_1_y < altura - raquete_altura:
        player_1_y += raquete_player_1_dy

    pygame.draw.rect (screen, VERDE, (pc_x,pc_y,raquete_largura,raquete_altura))
    pygame.draw.rect (screen, VERDE, (player_1_x,player_1_y,raquete_largura,raquete_altura))
    pygame.draw.ellipse(screen, bola_cor, (bola_x, bola_y, tamanho_bola, tamanho_bola))

    pygame.display.flip()

    clock.tick(40)

pygame.quit()
sys.exit()