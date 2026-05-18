import math

total_pregos = 0
while True:
    n = int(input())
    if n % 2 != 0: 
        break
    total_pregos += n

caixas = math.ceil(total_pregos / 12)
custo = caixas * 7.89
sobras = caixas * 12 - total_pregos

print(f"{custo:.2f}")
print(sobras)
