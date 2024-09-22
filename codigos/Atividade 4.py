import pygame as py

py.init()

tamanho_tela = (1300, 650)
popup = py.display.set_mode(tamanho_tela)
py.display.set_caption('Exercicio 4 - CG')

# Definir as variáveis para o quadrado
largura_quadrado = 25
altura_quadrado = 25
x_quadrado = 0  # Posição inicial
y_quadrado = 0  # Posição inicial
velocidade = 1  # Velocidade de movimento do quadrado

def desenhar_quadrado(x, y):
    # Cores
    cor_verde = (0, 255, 0)

    # Desenhando o quadrado
    py.draw.rect(popup, cor_verde, (x, y, largura_quadrado, altura_quadrado))

running = True

while running:
    for evento in py.event.get():
        if evento.type == py.QUIT:
            running = False

    # verificar quais teclas estão sendo pressionadas
    teclas = py.key.get_pressed()

    # Mover o quadrado para cima, baixo, esquerda ou direita
    if (teclas[py.K_w] or teclas[py.K_UP]) and y_quadrado > 0:
        y_quadrado -= velocidade
    if (teclas[py.K_s] or teclas[py.K_DOWN]) and y_quadrado < tamanho_tela[1] - altura_quadrado:
        y_quadrado += velocidade
    if (teclas[py.K_a] or teclas[py.K_LEFT]) and x_quadrado > 0:
        x_quadrado -= velocidade
    if (teclas[py.K_d] or teclas[py.K_RIGHT]) and x_quadrado < tamanho_tela[0] - largura_quadrado:
        x_quadrado += velocidade

    # Preencher o fundo com branco antes de desenhar o quadrado
    popup.fill((0, 0, 0)) 
    
    # Desenhar o quadrado na posição atualizada
    desenhar_quadrado(x_quadrado, y_quadrado)

    py.display.flip()

py.quit()