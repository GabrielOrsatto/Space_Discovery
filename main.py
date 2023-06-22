import pygame

#inicializar o pygame
pygame.init()
tamanho = (1000,563)

clock = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho )
icone = pygame.image.load("icone.ico")
pygame.display.set_icon( icone )
fundo = pygame.image.load("bg.jpg")
pygame.display.set_caption("Space Discovery")
pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play(-1)

space = pygame.image.load("space.png")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False    

        

    #aqui vai o código em si
    tela.blit(fundo, (0,0) )
    tela.blit(space, (50,30) )


    pygame.display.update()
    clock.tick(40)
    
pygame.quit()
