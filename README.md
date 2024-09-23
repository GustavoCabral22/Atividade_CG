# Atividade Avaliativa - Computação Gráfica e Realidade Virtual

Este repositório contém as soluções para a lista de exercícios práticos de Computação Gráfica. A atividade conta 10% da A3 e foi desenvolvida em grupo de 2 pessoas.

## **Alunos:**  

Gustavo dos Santos Cabral - RA: 12922110105  
Lucas Rodrigues Lança - RA: 1292216966

## Instruções de Uso:
**Passo 1:** Realizar o download da pasta, contendo os códigos  
**Passo 2:** Abrir uma IDE, ou outro software que seja possível rodar python (Google Colab, Replit, Etc)  
**Passo 3:** Dentro da IDE, abrir a pasta com os códigos  
**Passo 4:** Instalar as bibliotecas "pygame", "random" e "math"  no terminal, utilizando o comando "pip install pygame random math"  
**Passo 5:** Rodar os códigos

## Link do drive com fotos, vídeos e gifs dos códigos funcionando:
https://drive.google.com/drive/folders/1HzTA9lb5cJ20779yqSnHSR5RMKSGimO0?usp=drive_link

## Exercício 1   
### Descrição   
**Explicação:** Primeiro foi criada uma linha que divide a tela em 4 quadrantes, a linha sai do ponto (0,0). Em cima-esquerda está a letra "a", com um ponto vermelho centralizado;, Em cima-direita está a letra "b", usando variáveis para determinar 2 pontos dentro do qudrante, o usuário informa onde os pontos irão ficar e traça uma linha verde entre eles (para ficar dentro do quadrante o usuário deve digitar números inteiros positivos); Em baixo-direito está a letra "c" com um quadrado amarelo centralizado; Em baixo-esquerda está a letra "d", um triângulo equilátero rosa centralizado no seu quadrante.

## Exercício 2    
### Descrição
**Explicação:** Esse código usa o Pygame para criar uma tela e desenhar várias coisas, tipo umas linhas no meio que dividem a tela em quatro partes. Em cada parte, é colocado os triângulos de jeitos diferentes: uns cheios, uns só com o contorno, uns com pontos nos vértices, e por aí vai. A ideia é era juntar toda a lista de exercícios (a, b, c, d) em uma tela somente e mostrar como dá pra desenhar essas formas no Pygame.
 
## Exercício 3 
### Descrição   
**Explicação:** Primeiro foi criada uma linha que divide a tela em 4 quadrantes, a linha sai do ponto (0,0). É criada uma função para gerar um triângulo retângulo fazendo uso de variáveis. As setas direita e esquerda irão mover o triângulo no eixo x; as teclas cima e baixo irão aumentar o tamanho e diminuir o tamanho do triângulo; por fim as teclas "a" e "d" irão rotacionar o triângulo para direita e esquerda.

## Exercício 4   
### Descrição   
**Explicação:** Aqui o código cria uma tela com um quadrado verde que você pode mover usando as setas do teclado ou W, A, S, D. O quadrado começa num canto e vai se movendo de acordo com o que você apertar, apertando devagar porque a velocidade é de 1 pixel. A tela fica preta pra “limpar” o desenho anterior e mostrar o quadrado na nova posição. Foi feito assim pra mostrar como funciona o movimento básico de um objeto usando o teclado no Pygame.

## Exercício 5   
### Descrição   
**Explicação:** Primeiro foi criada uma linha que divide a tela em 4 quadrantes, a linha sai do ponto (0,0). O triângulo verde é refletido no eixo x; O circulo amarelo é refletido no eixo y; O quadrado vermelho é refletido tanto no eixo x quanto no eixo y. A linha divisória serve para melhorar a observação das formas e suas reflexões. 

## Exercício 6   
### Descrição   
**Explicação:** Esse código desenha uma casa bem simples na tela usando Pygame. Tem o corpo marrom, o telhado vermelho, duas janelinhas azuis e uma porta no meio. As formas e cores foram escolhidas pra ficar parecido com uma casa básica mesmo. A ideia era desenvolver melhor como desenhar utilizando formas geométricas e montar um desenho mais elaborado usando coisas simples como retângulos e triângulos. 

## Exercício 7   
### Descrição   
**Explicação:** Usando um retângulo verde para lembrar a grama, um retângulo azul para ser a casa, um retângulo laranja para ser uma porta, um ponto preto para ser uma maçaneta, um retângulo azul claro para ser uma janela, um triângulo vinho para ser o telhado, um circulo com um tom fraco de amarelo para ser uma lua, pontos brancos representando estrelas e por fim o fundo preto padrão do pygame, foi possível construir um cenário de uma casa colorida durante a noite.

## Exercício 8   
### Descrição   
**Explicação:** Aqui, a ideia foi montar um grid de quadrados coloridos aleatoriamente no meio da tela. Tem 10 linhas e 10 colunas, e cada quadrado tem 20x20 pixels. As cores são escolhidas de uma lista e colocadas aleatoriamente em cada quadrado. A ideia é mostrar como usar loops pra desenhar um monte de quadrados “certinhos” na tela e brincar com as cores (pois a cada vez que o código é executado, as cores mudam). Foi feito assim pra ver como posicionar as coisas e fazer um visual dinâmico e meio bagunçado com as cores.
