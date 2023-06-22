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
fonte = pygame.font.SysFont(None, 20)

space = pygame.image.load("space.png")

F10 = fonte.render("PRESSIONE F10 PARA SALVAR OS PONTOS", True, branco)
F11 = fonte.render("PRESSIONE F11 PARA CARREGAR OS PONTOS", True, branco)
F12 = fonte.render("PRESSIONE F12 PARA DELETAR OS PONTOS",True, branco)

running = True

estrelas = {}

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
                print(estrelas)


    tela.blit(fundo, (0,0) )
    tela.blit(space, (50,30) )
    tela.blit(F10, (690, 480))
    tela.blit(F11, (690, 500))
    tela.blit(F12, (690, 520))

    for nome, pos in estrelas.items(): 
        if nome != "":
            pygame.draw.circle(tela, branco, pos, 5)
            texto = fonte.render(nome, True, branco)
            tela.blit(texto, pos)

    if len(estrelas) >= 2:
        pontos = list(estrelas.values())
        pygame.draw.lines(tela, branco, False, pontos, 2)

    pygame.display.update()
    clock.tick(40)

pygame.quit()