age = int(input("escreva sua idade "))
time = int(input("escreva quantos anos voce trabalhou "))

if (age >= 65) or (time >= 30) or (age >= 60 and time >= 25):
    print("voce ja pode se aposentar")
else:
    print("voce ainda nao pode se aposentar")