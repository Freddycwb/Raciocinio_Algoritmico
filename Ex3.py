import string
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
import random

letter = str(input("escreva uma letra (letras maiusculas e minusculas fazem diferença) "))
sorted_letter = random.choice(string.ascii_letters)
hp = 5

while letter != sorted_letter:
    hp -= 1
    if hp < 0:
        break
    letter = str(input("escreva outra letra "))
if hp > 0:
    print("Ganhooo")
else:
    print("Perdeeeu")