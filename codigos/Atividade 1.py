
# Importa pygame e OpenGL

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Cria uma linha que divide a tela em 4 setores
def linha_divisoria():
    glColor3f(1.0, 1.0, 1.0)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(-800, 0)
    glVertex2f(800, 0)
    glVertex2f(0, -400)
    glVertex2f(0, 400)
    glEnd()

# No primeiro setor, é criado um ponto vermelho no centro do quadrante
# a)
def criar_ponto():
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2f(-400, 200)
    glEnd()

# Define 2 pontos dentro do segundo quadrante, sendo ele o positivo, logo depois, traça uma linha verde entre os pontos.
# b)
def criar_reta(x1, y1, x2, y2):
    glColor3f(0.0, 1.0, 0.0)
    glLineWidth(8)
    glBegin(GL_LINES)
    # Usado variaveis para interação com usuário
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

# Função para criação do quadrado amarelo centralizado no seu quadrante
# c)
def criar_quadrado():
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_QUADS)
    glVertex2f(300, -100)
    glVertex2f(500, -100)
    glVertex2f(500, -300)
    glVertex2f(300, -300)
    glEnd()

# Função para a criação de um triângulo equilátero rosa no seu quadrante
# d)
def criar_triangulo():
    glColor3f(1.0, 0.0, 1.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-400, -143)
    glVertex2f(-500, -257)
    glVertex2f(-300, -257)
    glEnd()

# Inicia pygame
pygame.init()

# Criação da janela
screen = pygame.display.set_mode((1600, 800), DOUBLEBUF | OPENGL)

# Proporções da tela
gluOrtho2D(-800, 800, -400, 400)

# Título da janela
pygame.display.set_caption("Atividade 1")

# Interação com o usuário para definir a linha verde
x1 = int(input("Digite x1 positivo: "))
y1 = int(input("Digite y1 positivo: "))
x2 = int(input("Digite x2 positivo: "))
y2 = int(input("Digite y2 positivo: "))

# Usado para testes mais rápidos dos outros exercicios
# x1 = 50
# y1 = 300
# x2 = 150
# y2 = 100

# Variável e função para rodar no pygame
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Código aqui

    # Chamando as funções
    linha_divisoria()
    criar_ponto()
    criar_reta(x1, y1, x2, y2)
    criar_quadrado()
    criar_triangulo()

    pygame.display.flip()

pygame.quit()