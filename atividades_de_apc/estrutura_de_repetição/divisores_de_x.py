numero = int(input())

for i in range(numero, 0, -1):  #começa em número e vai até 1
    if numero % i == 0:
        print(i)
