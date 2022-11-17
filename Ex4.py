matriz = []
xDiagonal = 0

def criaMatrix(x, y):
    novaMatriz = [[1]] * y
    for indice in range(y):
        novaMatriz[indice] = [1] * x
    return novaMatriz

matriz = criaMatrix(5, 5)

for indiceX in range(5):
    for indiceY in range(5):
        if indiceY == xDiagonal:
            matriz[indiceX][indiceY] = 0
            xDiagonal += 1
            break

for indice in range(len(matriz)):
    print(matriz[indice])