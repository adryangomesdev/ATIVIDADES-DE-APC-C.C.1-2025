peso_total = 18
peso = 0
quantidade = 0

while True:
    livros_colocados = int(input())
    peso += livros_colocados
    if  peso > 18:
        break
    else:
        quantidade += 1

print(f"{quantidade}")