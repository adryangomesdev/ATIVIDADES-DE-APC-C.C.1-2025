numero_competidores = int(input())
nota_convocado = int(input())
quantidade = 0

for i in range(1, numero_competidores + 1):
    nota1 = int(input())
    nota2 = int(input())
    if (nota1 + nota2) >= nota_convocado and nota1 != 0 and nota2 != 0:
        quantidade += 1

print(f"{quantidade}")