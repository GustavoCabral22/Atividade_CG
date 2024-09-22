import pygame as py
import random

py.init()

tamanho_tela = (800, 600) 
tamanho_quadrado = 20      
linhas = 10              
colunas = 10

popup = py.display.set_mode(tamanho_tela)
py.display.set_caption("Atividade 8")       

# Calcular o tamanho total do grid
largura_grid = colunas * tamanho_quadrado
altura_grid = linhas * tamanho_quadrado

cores = [
    (255, 0, 0),    # Vermelho
    (0, 255, 0),    # Verde
    (0, 0, 255),    # Azul
    (255, 255, 0),  # Amarelo
    (255, 0, 255),  # Rosa
    (255, 165, 0),  # Laranja
]

cor_fundo = (0, 0, 0)

# Função para gerar o grid de cores aleatórias
def gerar_cores_grid():
    grid_cores = []
    for _ in range(linhas):
        linha_cores = [random.choice(cores) for _ in range(colunas)]
        grid_cores.append(linha_cores)
    return grid_cores

# Função para desenhar o grid de quadrados coloridos
def desenhar_grid(grid_cores):
    # Calcular a posição inicial do grid para centralizar
    x_inicio = (tamanho_tela[0] - largura_grid) // 2
    y_inicio = (tamanho_tela[1] - altura_grid) // 2

    # Desenhar cada quadrado na posição calculada
    for i, linha in enumerate(grid_cores):
        for j, cor in enumerate(linha):
            x = x_inicio + j * tamanho_quadrado
            y = y_inicio + i * tamanho_quadrado
            py.draw.rect(popup, cor, (x, y, tamanho_quadrado, tamanho_quadrado))

# Gerar as cores para o grid uma vez
cores_grid = gerar_cores_grid()

running = True

while running:
    for evento in py.event.get():
        if evento.type == py.QUIT:
            running = False

    popup.fill(cor_fundo)
    desenhar_grid(cores_grid)
    py.display.flip()

py.quit()
