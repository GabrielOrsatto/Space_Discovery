import pygame

#inicializar o pygame
pygame.init()
tamanho = (1000,563)
branco = (255, 255, 255)
tela = pygame.display.set_mode( tamanho )

icone = pygame.image.load("icone.ico")
pygame.display.set_icon( icone )
fundo = pygame.image.load("bg.jpg")
pygame.display.set_caption("Space Discovery")
pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()

space = pygame.image.load("space.png")

running = True

circulos = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                circulos.append(event.pos)

    #aqui vai o código em si
    tela.blit(fundo, (0,0) )
    tela.blit(space, (50,30) )

    for posicao in circulos:
        pygame.draw.circle(tela, branco, posicao, 5)


    pygame.display.update()
    clock.tick(40)

    
pygame.quit()
