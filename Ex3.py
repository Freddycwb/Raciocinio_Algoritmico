linhas = int(input("Digite o numero de linhas da matriz "))
colunas = int(input("Digite o numero de colunas da matriz "))
matriz = []
impares = []

def criaMatrix(x, y):
    novaMatriz = [[0]] * y
    for indice in range(y):
        novaMatriz[indice] = [0] * x
    return novaMatriz

matriz = criaMatrix(colunas, linhas)

for indiceX in range(linhas):
    for indiceY in range(colunas):
        matriz[indiceX][indiceY] = int(input("Digite um valor da matriz "))


for indice in range(len(matriz)):
    print(matriz[indice])

for indiceX in range(linhas):
    for indiceY in range(colunas):
        if matriz[indiceX][indiceY] % 2 != 0:
            impares.append(matriz[indiceX][indiceY])

print("valores impares - ",impares)

print("menor valor - ", min(min(matriz)))