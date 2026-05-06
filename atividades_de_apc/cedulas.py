N = int(input())

print(N)

notas = [100, 50, 20, 10, 5, 2, 1]

for nota in notas:
    quantidade = N // nota
    print("{} nota(s) de R$ {},00".format(quantidade, nota))
    N = N % nota
