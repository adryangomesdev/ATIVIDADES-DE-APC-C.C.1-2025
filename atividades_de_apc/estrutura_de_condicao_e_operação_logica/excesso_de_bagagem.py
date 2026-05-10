peso = float(input())

if peso <= 20.0:
    print("0.00")
elif 20.0 < peso <= 25.0:
    taxa = (peso - 20.0) * 12.50
    print(f"{taxa:.2f}")
elif 25.0 < peso <= 30.0:
    taxa = (peso - 20.0) * 32.75
    print(f"{taxa:.2f}")
else:
    print("PESO LIMITE EXCEDIDO")
