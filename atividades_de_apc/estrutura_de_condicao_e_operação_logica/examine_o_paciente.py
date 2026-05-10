t = float(input())
s = input().strip().upper()  # remove espaços e deixa maiusculo

if t >= 37 and s == "S":
    print("Exames Especiais")
elif t >= 37 and s == "N":
    print("Exames Basicos")
elif t < 37 and s == "N":
    print("Liberado")
elif t < 37 and s == "S":
    print("Exames Basicos")
else:
    print("Erro")

