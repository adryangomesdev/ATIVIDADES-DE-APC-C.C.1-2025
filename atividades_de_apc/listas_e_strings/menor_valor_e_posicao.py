tamanho_array = int(input())
numero_lista = []

entrada = input().split()

for i in range(tamanho_array):
    numero = int(entrada[i])
    numero_lista.append(numero)

numero_minino = min(numero_lista)
posicao = numero_lista.index(numero_minino)

print(f"Menor valor: {numero_minino}")
print(f"Posicao: {posicao}")
