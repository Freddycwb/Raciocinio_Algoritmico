# Link do video do projeto 
# https://www.youtube.com/watch?v=7_bMinrqAvQ

from random import randrange

matrizEmbarcaçoesJogador = []
matrizEmbarcaçoesComputador = []

matrizTabuleiroJogador = []
matrizTabuleiroComputador = []

indice = 0

def criaMatrix():
    novaMatriz = [[0]] * 5
    for indice in range(5):
        novaMatriz[indice] = [0] * 10
    return novaMatriz

matrizEmbarcaçoesJogador = criaMatrix()
matrizEmbarcaçoesComputador = criaMatrix()
matrizTabuleiroJogador = criaMatrix()
matrizTabuleiroComputador = criaMatrix()

def definirElementoDaMatriz(matriz, linha, coluna, valor):
    for linhaAtual in range(5):
        for colunaAtual in range(10):
            if linhaAtual == linha and colunaAtual == coluna:
                matriz[linhaAtual][colunaAtual] = valor
                break
    return matriz

def pegarNumeroDeEmbarcações(matriz):
    valor = 0
    for linhaAtual in range(5):
        for colunaAtual in range(10):
            if matriz[linhaAtual][colunaAtual] == 1:
                valor += 1
    return valor

def mostrarMatriz(matriz):
    for linha in range(len(matriz)):
        print(matriz[linha])

print("-----------------------------------")
print("Bem vindo ao Batalha Naval!")

while indice < 5:
    linha = int(input("Em qual linha deseja posicionar a embarcação " + str(indice + 1) + "? "))
    coluna = int(input("Em qual coluna deseja posicionar a embarcação " + str(indice + 1) + "? "))
    linha -= 1
    coluna -= 1
    if linha >= 0 and linha <= 4 and coluna >= 0 and coluna <= 9 and matrizEmbarcaçoesJogador[linha][coluna] == 0:
        matrizEmbarcaçoesJogador = definirElementoDaMatriz(matrizEmbarcaçoesJogador, linha, coluna, 1)
    elif linha < 0 or linha > 4 or coluna < 0 or coluna > 9:
        indice -= 1
        print("Posição invalida, use numeros de 1 a 5 para as linhas e de 1 a 10 para as colunas")
    elif matrizEmbarcaçoesJogador[linha][coluna] != 0:
        indice -= 1
        print("Essa posição ja esta ocupada")
    indice += 1

indice = 0
while indice < 5:
    linha = randrange(0, 5)
    coluna = randrange(0, 10)
    if linha >= 0 and linha <= 4 and coluna >= 0 and coluna <= 9 and matrizEmbarcaçoesComputador[linha][coluna] == 0:
        matrizEmbarcaçoesComputador = definirElementoDaMatriz(matrizEmbarcaçoesComputador, linha, coluna, 1)
    elif linha < 0 or linha > 4 or coluna < 0 or coluna > 9:
        indice -= 1
        print("Posição invalida, use numeros de 1 a 5 para as linhas e de 1 a 10 para as colunas")
    elif matrizEmbarcaçoesComputador[linha][coluna] != 0:
        indice -= 1
        print("Essa posição ja esta ocupada")
    indice += 1

def mostrarTabuleiros():
    print("Tabuleiro do Computador")
    mostrarMatriz(matrizTabuleiroComputador)
    print("-----------------------------------")
    print("Embarcações restantes: ", pegarNumeroDeEmbarcações(matrizEmbarcaçoesComputador))
    print("")
    print("Tabuleiro do Jogador")
    mostrarMatriz(matrizTabuleiroJogador)
    print("-----------------------------------")
    print("Embarcações restantes: ", pegarNumeroDeEmbarcações(matrizEmbarcaçoesJogador))
    print("")

def ataqueDoJogador():
    linha = int(input("Qual linha deseja atacar? "))
    coluna = int(input("Qual coluna deseja atacar? "))
    linha -= 1
    coluna -= 1
    if matrizEmbarcaçoesComputador[linha][coluna] == 1:
        print("Parabéns! Você acertou!")
        print("")
        definirElementoDaMatriz(matrizTabuleiroComputador, linha, coluna, "X")
        definirElementoDaMatriz(matrizEmbarcaçoesComputador, linha, coluna, "X")
    else:
        print("Não foi dessa vez!")
        print("")
        definirElementoDaMatriz(matrizTabuleiroComputador, linha, coluna, "O")

def ataqueDoComputador():
    linha = randrange(0, 5)
    coluna = randrange(0, 10)
    print("Computador escolheu a linha ", linha)
    print("Computador escolheu a coluna ", coluna)
    if matrizEmbarcaçoesJogador[linha][coluna] == 1:
        print("Computador acertou!")
        print("")
        definirElementoDaMatriz(matrizTabuleiroJogador, linha, coluna, "X")
        definirElementoDaMatriz(matrizEmbarcaçoesJogador, linha, coluna, "X")
    else:
        print("Computador errou!")
        print("")
        definirElementoDaMatriz(matrizTabuleiroJogador, linha, coluna, "O")

while True:
    mostrarTabuleiros()
    ataqueDoJogador()
    if pegarNumeroDeEmbarcações(matrizEmbarcaçoesComputador) <= 0:
        print("Parabéns! Você afundou todas as embarcações do inimigo!")
        print("Jogo desenvolvido por: Freddy Matheus ,Leonardo Hideki, Mariana Pereira, Rodrigo Ribas")
        print("Obrigado por jogar nosso jogo!")
        break
    ataqueDoComputador()
    if pegarNumeroDeEmbarcações(matrizEmbarcaçoesJogador) <= 0:
        print("Que pena :( O computador afundou todas as suas embarcações!")
        print("Jogo desenvolvido por: Freddy Matheus ,Leonardo Hideki, Mariana Pereira, Rodrigo Ribas")
        print("Obrigado por jogar nosso jogo!")
        break
