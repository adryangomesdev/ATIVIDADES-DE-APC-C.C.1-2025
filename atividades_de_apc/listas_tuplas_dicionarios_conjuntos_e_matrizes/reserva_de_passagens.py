voos = {}

# Lê os 37 voos
for _ in range(37):
    numero, lugares = map(int, input().split())
    voos[numero] = lugares

# Processa os pedidos
while True:
    entrada = input().strip()
    
    if entrada == "9999":
        break  # encerra o programa

    doc, voo = map(int, entrada.split())
    
    # Verifica se o voo existe e há lugares
    if voo in voos and voos[voo] > 0:
        print(doc)
        voos[voo] -= 1  # reduz um assento
    else:
        print("INDISPONIVEL")