import pygame
import json
from tkinter import simpledialog

pygame.init()

tamanho = (1000,563)
tela = pygame.display.set_mode( tamanho )

icone = pygame.image.load("icone.ico")
pygame.display.set_icon( icone )

fundo = pygame.image.load("bg.jpg")

pygame.display.set_caption("Space Discovery")

pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

fonte = pygame.font.SysFont(None, 20)

branco = (255, 255, 255)
F10 = fonte.render('Pressione F10 para salvar os pontos', True, branco)
F11 = fonte.render('Pressione F11 para carregar os pontos', True, branco)
F12 = fonte.render('Pressione F12 para deletar os pontos', True, branco)

running = True

estrelas = {}

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F10:
            try:
                with open('db.txt','w') as database:
                    json.dump(estrelas,database)
            except:
                print("Erro ao criar base de dados")

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            try:
                with open('db.txt') as database:
                    estrelas = json.load(database)
            except:
                print("Erro ao salvar os pontos")

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F12:
            estrelas.clear()

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            posicaoEstrela = pygame.mouse.get_pos()
            nomeEstrela = simpledialog.askstring("Space", "Nome da Estrela: ")
            if nomeEstrela is not None:
                if nomeEstrela.strip() == "":
                    nomeEstrela = "Desconhecido"+str(posicaoEstrela)      
                estrelas[nomeEstrela] = posicaoEstrela
               
    tela.blit(fundo, (0,0))
    tela.blit(F10, (690, 480))
    tela.blit(F11, (690, 500))
    tela.blit(F12, (690, 520))

    for nomeEstrela, posicaoEstrela in estrelas.items():
        try:
            if nomeEstrela != "":
                pygame.draw.circle(tela, branco, posicaoEstrela, 5)
                texto = fonte.render(nomeEstrela, True, branco)
                tela.blit(texto, posicaoEstrela)
        except:
            print("Erro 273627x02. Reinicie a aplicação!")

        if len(estrelas) >= 2:
            pontos = list(estrelas.values())
            pygame.draw.lines(tela, branco, False, pontos, 1)
            with open('db.txt','w') as database:
                json.dump(estrelas,database)



        print('asjhdkjashdkja')

    pygame.display.update()
    clock.tick(40)

pygame.quit()