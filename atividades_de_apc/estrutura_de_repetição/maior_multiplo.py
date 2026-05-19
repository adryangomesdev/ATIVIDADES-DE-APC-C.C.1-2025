M = int(input())
N = int(input())

multiplo = 0
i = M

while i <= N:
    multiplo = i
    i += M

if multiplo == 0:
    print(f"sem multiplos menores que {N}")
else:
    print(multiplo)