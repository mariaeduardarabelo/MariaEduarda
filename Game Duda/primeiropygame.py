import pygame
#inicializar o pygame

pygame.init()
#cria uma tela com tamanho especificado
tamanho = (900,500)

tela = pygame.display.set_mode(tamanho)
#Define o título da janela
pygame.display.set_caption("Hello Games!")
#Define um relogio para controlar o FPS
relogio = pygame.time.Clock()

posicaoBola = pygame.Vector2(450,250)
dt = 0
direcaoy = 1
direcaox = 1

while True:
    #lida com os eventos da aplicação
    for evento in pygame.event.get():
        print(evento)
        if evento.type == pygame.QUIT:
            pygame.quit()

    #Preenche a tela com uma cor
    tela.fill((200,100,200))

    #Desenha um círculo na tela
    pygame.draw.circle(tela,(10,255,200), posicaoBola , 50)

    posicaoBola.y += 100 * direcaoy * dt
    
    if posicaoBola.y >= 450:
        direcaoy = -1

    elif posicaoBola.y <= 50:
        direcaoy += 1
        
    posicaoBola.x += 100 * direcaox * dt
    
    if posicaoBola.x >= 850:
        direcaox = -1

    elif posicaoBola.x <= 50:
        direcaox += 1
        

    #Atualiza a tela
    pygame.display.update()
    dt = relogio.tick(60) / 100 # Define a quantidade de FPS
    relogio.tick(60)