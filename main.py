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

estrelas = {}
posicoes = []


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            pos = pygame.mouse.get_pos()
            nome = simpledialog.askstring("Space", "Nome da Estrela: ")
            if nome is not None:
                if nome.strip() == "":
                    nome = "Desconhecido"+str(pos)       
                estrelas[nome] = pos
                posicoes.append(pos)
                print(nome)

    #aqui vai o código em si
    tela.blit(fundo, (0,0) )
    tela.blit(space, (50,30) )

    for nome, pos in estrelas.items(): 
        if nome != "":
            pygame.draw.circle(tela, branco, pos, 5)
            fonte = pygame.font.SysFont(None, 20)
            texto = fonte.render(nome, True, branco)
            tela.blit(texto, pos)
    for item in posicoes:
        if len(posicoes) >= 2:
            pygame.draw.lines(tela, branco, False, posicoes, 2)

    pygame.display.update()
    clock.tick(40)

pygame.quit()
