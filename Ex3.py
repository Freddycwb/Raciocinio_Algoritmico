vetor = []
maiores_que_cinco = []
soma_pares = 0
soma_impares = 0
soma = 0
valor = int(input("digite um valor maior ou igual a 0: "))

while valor >= 0:
    vetor.append(valor)
    if valor > 5:
        maiores_que_cinco.append(valor)
    if valor % 2 == 0:
        soma_pares += valor
    else:
        soma_impares += valor
    soma += valor
    valor = int(input("digite um valor (valores negativos param a aplicação): "))

# a.
print(vetor)
# b.
print("valores maiores que cinco ", len(maiores_que_cinco), maiores_que_cinco)
# c.
print("soma dos valores pares ", soma_pares)
# d.
print("soma dos valores impares ", soma_impares)
# e.
print("soma total ", soma)