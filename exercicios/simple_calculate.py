number_of_the_product = int(input())
number_of_products_sold = int(input())
price_of_the_products = float(input())
number_of_the_product2 = int(input())
number_of_products_sold2 = int(input())
price_of_the_products2 = float(input())

print("O número do produto número 1 é: " ,number_of_the_product)
print("Produtos comprados número 1: " ,number_of_products_sold)
print("Preço dos produtos número 1: %.2f" %price_of_the_products)
print("O número do produto número 2 é: " ,number_of_the_product2)
print("Produtos comprados número 2: " ,number_of_products_sold2)
print("Preço dos produtos número 2: %.2f" %price_of_the_products2)

total = (number_of_products_sold * price_of_the_products)
total2 = (number_of_products_sold2 * price_of_the_products2)

total3 = (total + total2)

print("Valor a pagar: R$ %.2f" %total3)