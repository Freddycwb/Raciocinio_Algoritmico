saldo = 0
request = 0
entrada = -1

print("1. consultar saldo")
print("2. saque.")
print("3. deposito.")
print("0. Sair")

while True:
    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 0:
        print("\ntchau >:(")
        break
    elif opcao == 1:
        print("esse é seu saldo ", saldo)
    elif opcao == 2:
        request = float(input("digite quanto quer sacar "))
        if request > saldo:
            print("voce nao tem saldo suficiente")
        else:
            saldo -= request
            print("saque concluido, saldo restante ", saldo)
    elif opcao == 3:
        request = float(input("digite quanto quer depositar "))
        saldo += request
        print("deposito concluido, saldo atual ", saldo)