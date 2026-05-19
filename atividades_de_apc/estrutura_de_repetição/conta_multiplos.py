n = int(input())
n2 = int(input())
soma = 0

for i in range(1, 50):
    if i % n == 0 and i % n2 == 0:
        soma += 1

print(soma)