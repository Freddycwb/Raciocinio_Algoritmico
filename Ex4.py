vetor = [0] * 6
indice = 0

while indice < len(vetor):
    valor = int(input("digite um valor: "))
    vetor[indice] = valor
    indice += 1

while indice > 0:
    indice -= 1
    print(vetor[indice])