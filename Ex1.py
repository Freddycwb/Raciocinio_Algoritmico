value = float(input("escreva um valor"))
bigger = value
count = 0

while count < 2:
    print("o maior valor ate agora é ", bigger)
    value = float(input("escreva outro valor"))
    if bigger < value:
        bigger = value
    count += 1
print("o maior valor digitado foi ", bigger)