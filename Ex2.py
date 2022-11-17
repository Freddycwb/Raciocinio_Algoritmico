from random import randrange

dado = [1, 2, 3, 4, 5, 6]
player1 = []
player2 = []
jogando = True
resposta = 1
vezDoJogador1 = True

def jogarDado():
    valor = randrange(dado[0], len(dado) + 1)
    if vezDoJogador1:
        print("Jogador 1 jogou o dado")
        player1.append(valor)
        print("Caiu ", valor)
    else:
        print("Jogador 2 jogou o dado")
        player2.append(valor)
        print("Caiu ", valor)


while jogando:
    print("Digite '1' para começar")
    print("Digite '2' para encerrar")
    resposta = int(input("Resposta: "))
    if resposta == 1:
        jogarDado()
        vezDoJogador1 = not vezDoJogador1
    else:
        jogando = False

print("Jogadas do Jogador 1: ", player1)
print("Jogadas do Jogador 2: ", player2)
print("Soma dos valores do Jogador 1: ", sum(player1))
print("Soma dos valores do Jogador 2: ", sum(player2))
if sum(player1) > sum(player2):
    print("Jogador 1 é o vencedor")
elif sum(player1) < sum(player2):
    print("Jogador 2 é o vencedor")
else:
    print("Empate")



