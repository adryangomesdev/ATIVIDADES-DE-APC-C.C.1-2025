# Leitura dos 9 valores inteiros
valores = [int(input()) for _ in range(9)]

# Monta a matriz 3x3
matriz = [valores[i:i+3] for i in range(0, 9, 3)]

# Calcula a media
media = sum(valores) / 9

# Maior valor
maior = max(valores)

# Delta (1 se positivo, -1 se negativo, 0 se zero)
if maior > 0:
    delta = 1
elif maior < 0:
    delta = -1
else:
    delta = 0

# Soma da diagonal principal
soma_diag = matriz[0][0] + matriz[1][1] + matriz[2][2]

# Saída formatada
print(f"{media:.2f} {maior} {delta} {soma_diag}")