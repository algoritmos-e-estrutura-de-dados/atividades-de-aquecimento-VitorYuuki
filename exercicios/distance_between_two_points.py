import math

x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())

distance = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

print("O valor é de: %.4f" %distance)