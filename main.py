import pygame
from tkinter import simpledialog

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
estrelas  = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
             pos = pygame.mouse.get_pos()
             circulos.append(pos)
             item = simpledialog.askstring("Space", "Nome da Estrela: ")
             print(item)
             if item == None:
                item = "Desconhecido" + ": " + str(pos)
                estrelas.append((item, pos))
                print(item)

    #aqui vai o código em si
    tela.blit(fundo, (0,0) )
    tela.blit(space, (50,30) )

    for pos in circulos:
        pygame.draw.circle(tela, branco, pos, 5)

    for nome, pos in estrelas: 
        texto = nome
        fonte = pygame.font.SysFont(None, 20)
        textoCor = fonte.render(texto, True, (255, 255, 255))
        tela.blit(textoCor, pos)

    pygame.display.update()
    clock.tick(40)

    
pygame.quit()
