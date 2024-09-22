
# Importa pygame e OpenGL

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

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

# Função para criação da imagem do triângulo
# a)
def triangulo():
    glColor3f(0, 1, 0)
    glBegin(GL_TRIANGLES)

    #Triangulo Original
    glVertex2f(400, 200)
    glVertex2f(300, 0)
    glVertex2f(500, 0)

    #Triangulo Espelhado
    glVertex2f(400, -200)
    glVertex2f(300, 0)
    glVertex2f(500, 0)
    glEnd()

# Função para criação de um circulo
# b)
def circulo(sx, sy, raio, seg):
    glColor3f(1, 0, 1)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(sx, sy)
    # Importação do pacote math para gerar o círculo
    for i in range(seg + 1):
        angulo = 2 * math.pi * i / seg
        x = sx + raio * math.cos(angulo)
        y = sy + raio * math.sin(angulo)
        glVertex2f(x, y)
    glEnd()

# Função para criação do quadrado
# c)
def quadrado():
    glColor3f(1, 0, 0)
    glBegin(GL_QUADS)

    # Quadrado Principal
    glVertex2f(0, 100)
    glVertex2f(100, 100)
    glVertex2f(100, 0)
    glVertex2f(0, 0)

    # Reflexo 3 nas linhas x e y
    glVertex2f(0, -100)
    glVertex2f(-100, -100)
    glVertex2f(-100, 0)
    glVertex2f(0, 0)

    # TESTES ANTERIORES

    # Reflexo 1 na linha do X
    # glVertex2f(-100, 100)
    # glVertex2f(0, 100)
    # glVertex2f(0, 0)
    # glVertex2f(-100, 0)
    #
    # Reflexo 2 na linha do Y
    # glVertex2f(0, 0)
    # glVertex2f(100, 0)
    # glVertex2f(100, -100)
    # glVertex2f(0, -100)

    glEnd()

# Inicia pygame
pygame.init()

# Criação da janela
screen = pygame.display.set_mode((1600, 800), DOUBLEBUF | OPENGL)

# Proporções da tela
gluOrtho2D(-800, 800, -400, 400)

# Título da janela
pygame.display.set_caption("Atividade 5")

# Variável e função para rodar no pygame
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Código aqui

    triangulo()
    quadrado()
    # Primeiro círculo
    circulo(100, 250, 100, 30)
    # Reflexo do círculo
    circulo(-100, 250, 100, 30)
    linha_divisoria()

    pygame.display.flip()

pygame.quit()