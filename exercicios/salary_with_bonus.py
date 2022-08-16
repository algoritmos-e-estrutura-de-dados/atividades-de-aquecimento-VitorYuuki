nome = input()
salary = float(input())
sales = float(input())

bonus = sales - (sales * 0.85)
salary_with_bonus = (bonus + salary)

print("Name of the employee: " ,nome)
print("Salário total: R$ %.2f" %salary_with_bonus)