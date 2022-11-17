lista = []
tamanho = int(input("Digite o tamanho da lista "))
contador = 0

def criaLista(numero):
    novaLista = [0] * numero
    return novaLista

lista = criaLista(tamanho)

while contador < len(lista):
    lista[contador] = int(input("Digite um dos valores da lista "))
    contador += 1

print("Lista - ",lista)
print("Lista reversa - ",lista[::-1])
print("Soma de todos os valores - ",sum(lista))
print("Menor numero da lista - ",min(lista))