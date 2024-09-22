import pygame as py

py.init()

tamanho_tela = (1300, 650)
popup = py.display.set_mode(tamanho_tela)
py.display.set_caption('Exercicio 2 - CG')

def linhas_na_tela():
    # Cores
    cor_laranja = (255, 165, 0)
    
    # Calculando os pontos centrais da tela
    meio_x = tamanho_tela[0] // 2  # Meio da largura (1300/2 = 650)
    meio_y = tamanho_tela[1] // 2  # Meio da altura (650/2 = 325)
    
    # Fazendo uma linha vertical e horizontal no meio da tela (formato "|", "--")
    py.draw.line(popup, cor_laranja, (meio_x, 0), (meio_x, tamanho_tela[1]), 2)  # linha vertical
    py.draw.line(popup, cor_laranja, (0, meio_y), (tamanho_tela[0], meio_y), 2)  # linha horizontal

def triangulos_preenchidos():
    # Definindo os vértices para caber na primeira parte da tela
    triangulo_1 = [[50, 150], [150, 150], [100, 50]]
    triangulo_2 = [[375, 150], [475, 150], [425, 50]]

    # Cores
    cor_azul = (0, 0, 255)  # Azul para o primeiro triângulo
    cor_vermelha = (255, 0, 0)  # Vermelho para o segundo triângulo

    # Desenhar os triângulos
    py.draw.polygon(popup, cor_azul, triangulo_1)
    py.draw.polygon(popup, cor_vermelha, triangulo_2)
    
    # Definindo a fonte e inserindo texto 
    fonte = py.font.Font(None, 24)  # Fonte padrão, tamanho 36
    texto = fonte.render('Exercício 1 - Letra A', True, (255, 255, 255))  # Texto na cor preta
    popup.blit(texto, (190, 10))  # Posicionar o texto acima do triângulo


def triangulo_com_contorno():
    # Definindo os vértices para caber na segunda parte da tela
    triangulo_1 = [[700, 150], [800, 150], [750, 50]]
    triangulo_2 = [[1025, 150], [1125, 150], [1075, 50]]
    
    # Cores
    cor_azul = (0, 0, 255)  # Azul para o primeiro triângulo
    cor_vermelha = (255, 0, 0)  # Vermelho para o segundo triângulo
    
    # Desenhar os triângulos
    py.draw.lines(popup, cor_azul, True, triangulo_1, 2)
    py.draw.lines(popup, cor_vermelha, True, triangulo_2, 2)
    
    # Definindo a fonte e inserindo texto
    fonte = py.font.Font(None, 24)  # Fonte padrão, tamanho 36
    texto = fonte.render('Exercício 1 - Letra B', True, (255, 255, 255))  # Texto na cor preta
    popup.blit(texto, (850, 10))  # Posicionar o texto acima do triângulo


def triangulo_sem_contorno():
    # Definindo os vértices para caber na terceira parte da tela
    triangulo_1 = [[50, 475], [150, 475], [100, 375]]
    triangulo_2 = [[375, 475], [475, 475], [425, 375]]
    
    # Cores
    cor_azul = (0,0,255)
    cor_vermelha = (255,0,0) 
    
    # Desenhar os triângulos
    for ponto in triangulo_1:
        py.draw.circle(popup, cor_azul, ponto, 5)
        
    for ponto in triangulo_2:
        py.draw.circle(popup, cor_vermelha, ponto, 5)
        
    # Definindo a fonte e inserindo texto
    fonte = py.font.Font(None, 24)  # Fonte padrão, tamanho 36
    texto = fonte.render('Exercício 1 - Letra C', True, (255, 255, 255))  # Texto na cor preta
    popup.blit(texto, (190, 335))  # Posicionar o texto acima do triângulo
    

def triangulo_com_3_formas():
    # Definindo os vértices para caber na quarta parte da tela
    triangulo_1 = [[700, 475], [800, 475], [750, 375]]
    triangulo_2 = [[1025, 475], [1125, 475], [1075, 375]]
    
    # Cores
    cor_azul = (0, 0, 255)
    cor_vermelha = (255, 0, 0)
    cor_verde = (0, 255, 0)
    
    # Desenhar os triângulos
    py.draw.polygon(popup, cor_azul, triangulo_1)
    py.draw.polygon(popup, cor_vermelha, triangulo_2) 
    
    # Desenhar os vértices dos triângulos como pontos verdes
    for ponto in triangulo_1:
        py.draw.circle(popup, cor_verde, ponto, 5)  # 5 pixels

    for ponto in triangulo_2:
        py.draw.circle(popup, cor_verde, ponto, 5) # 5 pixels
        
    # Definindo a fonte e inserindo texto
    fonte = py.font.Font(None, 24)  
    texto = fonte.render('Exercício 1 - Letra D', True, (255, 255, 255))  # Texto na cor branca
    popup.blit(texto, (850, 335))  # Posicao texto
    
running = True

while running:
    for evento in py.event.get():
        if evento.type == py.QUIT:
            running = False
            exit()

    linhas_na_tela()
    triangulos_preenchidos()
    triangulo_com_contorno()
    triangulo_sem_contorno()
    triangulo_com_3_formas()
    
    py.display.flip()
    popup.fill((0, 0, 0))

py.quit()