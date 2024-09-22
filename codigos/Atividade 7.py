
# Importa pygame e OpenGL

import math
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Retângulo que representa o chão
def fazer_chao():
    glColor3f(0, 1, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-800, -200)
    glVertex2f(800, -200)
    glVertex2f(800, -400)
    glVertex2f(-800, -400)
    glEnd()

# Quadrado que representa a casa
def fazer_casa():
    glColor3f(0.3, 0.5, 1)  # Cor branca
    glBegin(GL_QUADS)
    glVertex2f(-250, 20)
    glVertex2f(250, 20)
    glVertex2f(250, -200)
    glVertex2f(-250, -200)
    glEnd()

# Retângulo que representa porta
def fazer_porta():
    glColor3f(0.8, 0.5, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-200, -70)
    glVertex2f(-120, -70)
    glVertex2f(-120, -200)
    glVertex2f(-200, -200)
    glEnd()

# Ponto que representa uma maçaneta
def fazer_macaneta():
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(7)
    glBegin(GL_POINTS)
    glVertex2f(-130, -140)
    glEnd()

# Retângulo que serve como janela
def fazer_janela():
    glColor3f(0.0, 0.8, 0.8)
    glBegin(GL_QUADS)
    glVertex2f(-90, -70)
    glVertex2f(205, -70)
    glVertex2f(205, -170)
    glVertex2f(-90, -170)
    glEnd()

# Triângulo que serve como telhado
def fazer_telhado():
    glColor3f(0.5, 0.2, 0.4)
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 200)
    glVertex2f(-265, 20)
    glVertex2f(265, 20)
    glEnd()

# Círculo que serve como lua
def fazer_lua(sx, sy, raio, seg):
    glColor3f(1.0, 1.0, 0.6)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(sx, sy)  # Centro do círculo
    for i in range(seg + 1):
        angulo = 2 * math.pi * i / seg
        x = sx + raio * math.cos(angulo)
        y = sy + raio * math.sin(angulo)
        glVertex2f(x, y)
    glEnd()

# Pontos que servem para represnetar estrelas
def fazer_nuvens():
    glColor3f(0.9, 0.9, 0.9)  # Cor branca
    glPointSize(15)
    glBegin(GL_POINTS)
    glVertex2f(-680, 370)
    glVertex2f(-550, 320)
    glVertex2f(-600, 200)
    glVertex2f(-720, 280)
    glEnd()

# Inicia pygame
pygame.init()

# Criação da janela
screen = pygame.display.set_mode((1600, 800), DOUBLEBUF | OPENGL)

# Proporções da tela
gluOrtho2D(-800, 800, -400, 400)

# Título da janela
pygame.display.set_caption("Atividade 7")

# Variável e função para rodar no pygame
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Código aqui
    # Funções chamadas em ordem para serem sobrepostas corretamente
    fazer_chao()
    fazer_casa()
    fazer_porta()
    fazer_macaneta()
    fazer_janela()
    fazer_telhado()
    fazer_lua(580, 280, 100, 30)
    fazer_nuvens()

    pygame.display.flip()

pygame.quit()