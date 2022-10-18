vetor = [0] * 10
indice = 0
comparador = 0

repetidos = []

while indice < len(vetor):
    valor = int(input("digite um valor: "))
    vetor[indice] = valor
    indice += 1

for elemento in vetor:
    indice = 0
    while comparador < len(vetor):
        if elemento == vetor[comparador] and indice != comparador:
            print(elemento)
            repetidos.append(elemento)
        comparador += 1
    comparador = 0
    indice += 1