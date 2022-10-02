import math

a = int(input())
b = int(input())
c = int(input())

maior = (a + b + abs(a - b)) / 2

resultado = (maior + c + abs(maior - c)) / 2

print("O maior número é: " ,resultado)
