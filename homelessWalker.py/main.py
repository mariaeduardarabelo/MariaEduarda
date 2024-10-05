import pygame

pygame.init()

relogio = pygame.time.Clock()
tamanho = (1200, 500)
tela = pygame.display.set_mode(tamanho)

pygame.display.set_caption("Homelees Walker")
dt = 0

folhaSpritesWalk = pygame.image.load("assets/Homeless_1/Walk.png").convert_alpha()
folhaSpritesWalk = pygame.image.load("assets/Homeless_1/Walk.png").convert_alpha()

#define os frames
framesWalk = []

for i in range(6):
    frame = folhaSpritesWalk.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256,256))
    framesWalk.append(frame)

#variaveis da animaçao do personagem parado = 0
indexFrameWalk = 0
tempoAnimacaoWalk = 0.0
velocidadeAnimacaoWalk = 10

personagemRect = framesWalk[0].get_rect(midbottom = (100, 480))
gravidade = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    tela.fill((255,255,255))

    #Atualiza a animação do personagem parado
    tempoAnimacaoWalk += dt

    if tempoAnimacaoWalk >= 1 / velocidadeAnimacaoWalk:
        indexFrameWalk = (indexFrameWalk + 1) % len(framesWalk)
        tempoAnimacaoWalk = 0.0


    #Movimenta o personagem no eixo x
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        personagemRect.x -=100 * dt
    if teclas[pygame.K_RIGHT]:
        personagemRect.x +=100 * dt
    if teclas [pygame.K_SPACE]:
        if personagemRect.centery == 330:
            gravidade = -30

    #Gravidade aumenta
    gravidade += 3

    personagemRect.y += gravidade

    if personagemRect.centery >=330:
        personagemRect.centery = 330

    # if teclas[pygame.K_]:
    #   personagemRect.x -=100 * dt
    # if teclas[pygame.K_DOWN]:
    #     personagemRect.y +=100 * dt

    #Desenha o personagem
    tela.blit(framesWalk[indexFrameWalk],personagemRect)

    #pygame.draw.rect(tela, (0, 0, 0), personagemRect, 2)

    pygame.display.update()
    dt = relogio.tick(60)/1000