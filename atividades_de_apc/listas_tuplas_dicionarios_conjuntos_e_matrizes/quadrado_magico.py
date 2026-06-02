N = int(input())


matriz = [list(map(int, input().split())) for _ in range(N)]

# Soma de referencia: soma da primeira linha
soma_ref = sum(matriz[0])
magico = True

# Verifica as somas das linhas
for linha in matriz:
    if sum(linha) != soma_ref:
        magico = False
        break

# Verifica as somas das colunas
if magico:
    for c in range(N):
        soma_coluna = sum(matriz[l][c] for l in range(N))
        if soma_coluna != soma_ref:
            magico = False
            break

# Verifica diagonais
if magico:
    diag1 = sum(matriz[i][i] for i in range(N))
    diag2 = sum(matriz[i][N - 1 - i] for i in range(N))
    if diag1 != soma_ref or diag2 != soma_ref:
        magico = False

# Resultado final
if magico:
    print(soma_ref)
else:
    print(-1)