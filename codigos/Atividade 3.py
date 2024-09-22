
# Importa pygame e OpenGL

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Cria uma linha que divide a tela em 4 setores
def linha_divisoria():
    glColor3f(1.0, 1.0, 1.0)
    glLineWidth(0.5)
    glBegin(GL_LINES)
    glVertex2f(-800, 0)
    glVertex2f(800, 0)
    glVertex2f(0, -400)
    glVertex2f(0, 400)
    glEnd()

# Função de criação do triângulo
def triangulo(x, y):
    glBegin(GL_TRIANGLES)
    # lógica é usada para criar um triângulo retângulo
    glVertex2f(x, y)
    glVertex2f(x + 100 * tamanho, y)
    glVertex2f(x, y + 50 * tamanho)
    glEnd()

# Definição do x e y do triângulo, velocidade de movimento, tamanho oficial, posição de rotação inicial
tx, ty = 0, 0
velocidade = 0.2
tamanho = 1.0
rotacao = 0.0

# Inicia pygame
pygame.init()

# Criação da janela
screen = pygame.display.set_mode((1600, 800), DOUBLEBUF | OPENGL)

# Proporções da tela
gluOrtho2D(-800, 800, -400, 400)

# Título da janela
pygame.display.set_caption("Atividade 3")

# Variável e função para rodar no pygame
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Código aqui

    linha_divisoria()

    # Define as teclas para manipular o triângulo
    keys = pygame.key.get_pressed()

    # a)
    if keys[K_LEFT]:
        # Seta da esquerda para movimentar o triângulo no x para a direita
        tx -= velocidade
    if keys[K_RIGHT]:
        # Seta da direita para movimentar o triângulo no x para a direita
        tx += velocidade

    # b)
    if keys[K_UP]:
        # Seta para cima para aumentar o tamanho do triângulo
        tamanho += 0.001
    if keys[K_DOWN]:
        # Seta para cima para diminuir o tamanho do triângulo
        tamanho -= 0.001
        # Verificação para que o triângulo não fique menor a ponto de sumir
        if tamanho < 0.1:
            tamanho = 0.1

    # c)
    if keys[K_a]:
        # Botão "a" gira o triângulo para a esquerda
        rotacao -= 0.05
    if keys[K_d]:
        # Botão "d" gira o triângulo para a direita
        rotacao += 0.05

    # Metodo de lógica utilizado para fazer o movimento de rotação do triângulo
    glPushMatrix()
    glTranslatef(tx + 50 * tamanho, ty + 25 * tamanho, 0)
    glRotatef(rotacao, 0, 0, 1)
    glTranslatef(-(tx + 50 * tamanho), -(ty + 25 * tamanho), 0)

    triangulo(tx, ty)
    glPopMatrix()

    pygame.display.flip()

pygame.quit()
