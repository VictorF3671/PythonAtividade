num = int(input("Digite um número: "))

result = 1

for i in range(2, num + 1):
    result *= i

print(f"O fatorial de {num} é {resultado}")