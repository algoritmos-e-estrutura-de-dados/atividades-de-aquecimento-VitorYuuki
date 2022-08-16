x = int(input())
y = float(input())

print("Quilômetros andados: " ,x)
print("Litros de gasolina consumidos: " ,y)

km_l = (x / y)

print("A quantidade de kms que um automóvel consegue andar a cada 1 litro é de: %.3f" %km_l, "km/l")
