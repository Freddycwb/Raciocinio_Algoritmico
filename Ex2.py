from random import randint

vetor = [0] * 50
indice = 0
soma = 0
numeros_nove = 0
maior_numero = 0
menor_numero = 20

while indice < len(vetor):
    vetor[indice] = randint(0,20)
    soma += vetor[indice]
    if vetor[indice] == 9:
        numeros_nove += 1
    if vetor[indice] > maior_numero:
        maior_numero = vetor[indice]
    if vetor[indice] < menor_numero:
        menor_numero = vetor[indice]
    indice += 1

print(vetor)

# a.
print("soma ", soma)
# b.
print("ocorrencias do valor 9 ", numeros_nove)
# c.
print("maior valor ", maior_numero)
# d.
print("menor valor ", menor_numero)