Y = int(input())
cont_Y = 0
soma = 0
qtd = 0

for _ in range(20):
    x = int(input())
    if x == -1:
        break
    if x == Y:
        cont_Y += 1
    if x > 0 and not (15 <= x <= 20):
        soma += x
        qtd += 1

print(f"O número {Y} apareceu {cont_Y} vez(es)")

if qtd > 0:
    media = soma / qtd
    print(f"A média dos números foi de: {media:.2f}")
else:
    print("Sem valores para calcular a média")
