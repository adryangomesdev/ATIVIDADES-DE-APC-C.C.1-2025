numero_de_bois = int(input())
dicionario_de_bois = {}

for i in range(numero_de_bois):
    identificacao = input().split()
    id_do_boi = int(identificacao[0])
    peso_boi = float(identificacao[1])
    dicionario_de_bois[id_do_boi] = peso_boi

id_gordo, peso_gordo = max(dicionario_de_bois.items(), key=lambda item: item[1])
id_magro, peso_magro = min(dicionario_de_bois.items(), key=lambda item: item[1])

print(f"Gordo: id: {id_gordo} peso: {peso_gordo:.2f}Kg")
print(f"Magro: id: {id_magro} peso: {peso_magro:.2f}Kg")
