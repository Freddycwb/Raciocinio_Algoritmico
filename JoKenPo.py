import random
from time import sleep

print("Digite 1 para jogador vs jogador")
print("Digite 2 para jogador vs computador")
print("Digite 3 para computador vs computador")

modo_de_jogo = int(input("Digite o modo de jogo : "))

escolha_jogador1 = 0
escolha_jogador2 = 0

vitorias_jogador1 = 0
vitorias_jogador2 = 0
empates = 0

continuar_jogando = 1

def match():
  global vitorias_jogador1
  global vitorias_jogador2
  global empates
  if escolha_jogador1 == 1 and escolha_jogador2 == 2:
      print("Jogador 1 escolheu PEDRA e Jogador 2 escolheu PAPEL")
      print("Jogador 2 venceu!!!")
      vitorias_jogador2 = vitorias_jogador2 + 1
  elif escolha_jogador1 == 2 and escolha_jogador2 == 3:
      print("Jogador 1 escolheu PAPEL e Jogador 2 escolheu TESOURA")
      print("Jogador 2 venceu!!!")
      vitorias_jogador2 = vitorias_jogador2 + 1
  elif escolha_jogador1 == 3 and escolha_jogador2 == 1:
      print("Jogador 1 escolheu TESOURA e Jogador 2 escolheu PEDRA")
      print("Jogador 2 venceu!!!")
      vitorias_jogador2 = vitorias_jogador2 + 1
  elif escolha_jogador2 == 1 and escolha_jogador1 == 2:
      print("Jogador 1 escolheu PAPEL e Jogador 2 escolheu PEDRA")
      print("Jogador 1 venceu!!!")
      vitorias_jogador1 = vitorias_jogador1 + 1
  elif escolha_jogador2 == 2 and escolha_jogador1 == 3:
      print("Jogador 1 escolheu TESOURA e Jogador 2 escolheu PAPEL")
      print("Jogador 1 venceu!!!")
      vitorias_jogador1 = vitorias_jogador1 + 1
  elif escolha_jogador2 == 3 and escolha_jogador1 == 1:
      print("Jogador 1 escolheu PEDRA e Jogador 2 escolheu TESOURA")
      print("Jogador 1 venceu!!!")
      vitorias_jogador1 = vitorias_jogador1 + 1
  elif escolha_jogador1 == escolha_jogador2:
      print("Empate")
      empates = empates + 1
  else:
      print("Valor invalido")
      print("Partida cancelada")

def end():
    global continuar_jogando
    print("Jogador 1 - " + str(vitorias_jogador1))
    print("Jogador 2 - " + str(vitorias_jogador2))
    print("Empates : " + str(empates))
    print("Digite 1 para continuar")
    print("Digite 2 para sair")
    continuar_jogando = int(input("Quer continuar? : "))

while True:
    if modo_de_jogo == 1:
        print("Digite 1 para usar PEDRA")
        print("Digite 2 para usar PAPEL")
        print("Digite 3 para usar TESOURA")
        escolha_jogador1 = int(input("Jogador 1 , Digite sua escolha : "))
        escolha_jogador2 = int(input("Jogador 2 , Digite sua escolha : "))
        sleep(1)
        match()
        end()
    elif modo_de_jogo == 2:
        print("Digite 1 para usar PEDRA")
        print("Digite 2 para usar PAPEL")
        print("Digite 3 para usar TESOURA")
        escolha_jogador1 = int(input("Jogador 1 , Digite sua escolha : "))
        escolha_jogador2 = random.randint(1, 3)
        sleep(1)
        match()
        end()
    elif modo_de_jogo == 3:
        escolha_jogador1 = random.randint(1, 3)
        escolha_jogador2 = random.randint(1, 3)
        sleep(1)
        match()
        end()
    else:
        print("Modo invalido, por favor digite o modo 1, 2 ou 3")
        print("Digite 1 para jogador vs jogador")
        print("Digite 2 para jogador vs computador")
        print("Digite 3 para computador vs computador")
        modo_de_jogo = int(input("Digite o modo de jogo : "))
    if continuar_jogando == 2:
        print("Jogador 1 - " + str(vitorias_jogador1))
        print("Jogador 2 - " + str(vitorias_jogador2))
        print("Empates - " + str(empates))
        print("Obrigado por jogar")
        print("Freddy Matheus Goncalves")
        break

