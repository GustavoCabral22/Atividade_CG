import pygame as py

py.init()

tamanho_tela = (800, 600)
popup = py.display.set_mode(tamanho_tela)
py.display.set_caption("Exercício 6")

# Definir as cores
cor_casa = (150, 75, 0)      # Marrom para o corpo da casa
cor_telhado = (255, 0, 0)    # Vermelho para o telhado
cor_janela = (0, 191, 255)   # Azul para as janelas

def desenhar_casa():
    # Corpo da casa
    x_casa = 300
    y_casa = 300
    largura_casa = 200
    altura_casa = 120
    py.draw.rect(popup, cor_casa, (x_casa, y_casa, largura_casa, altura_casa))

    # Desenhar telhado
    ponto_1 = (x_casa, y_casa)                     # Canto inferior esquerdo do triângulo
    ponto_2 = (x_casa + largura_casa, y_casa)      # Canto inferior direito do triângulo
    ponto_3 = (x_casa + largura_casa // 2, y_casa - 100)  # Ponto do topo do triângulo
    py.draw.polygon(popup, cor_telhado, [ponto_1, ponto_2, ponto_3])

    # Desenhar janelas
    raio_janela = 15
    py.draw.circle(popup, cor_janela, (x_casa + 50, y_casa + 50), raio_janela) # Janela esquerda
    py.draw.circle(popup, cor_janela, (x_casa + 150, y_casa + 50), raio_janela) # Janela direita
    
    # Porta
    largura_porta = 30
    altura_porta = 40
    x_porta = x_casa + (largura_casa // 2) - (largura_porta // 2)  # Centralizar a porta na casa
    y_porta = y_casa + altura_casa - altura_porta
    py.draw.rect(popup, cor_janela, (x_porta, y_porta, largura_porta, altura_porta))

running = True

while running:
    for evento in py.event.get():
        if evento.type == py.QUIT:
            running = False

    popup.fill((0, 0, 0))
    desenhar_casa()

    py.display.flip()

py.quit()
