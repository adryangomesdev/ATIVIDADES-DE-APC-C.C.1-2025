# Lê as dimensões das matrizes
N, M, O = map(int, input().split())

# Lê a matriz A
A = [list(map(int, input().split())) for _ in range(N)]

# Lê a matriz B
B = [list(map(int, input().split())) for _ in range(M)]

# Inicializa a matriz C com zeros
C = [[0 for _ in range(O)] for _ in range(N)]

# Multiplicação de matrizes
for i in range(N):
    for j in range(O):
        for k in range(M):
            C[i][j] += A[i][k] * B[k][j]

# Imprime a matriz resultante
for linha in C:
    print(*linha)