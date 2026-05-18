matricula_menor = ""
menor_cre = float("inf")
soma_cre = 0
contador = 0

while True:
    matricula = str(input())
    if matricula == "999":
        break
    cre = float(input())
    
    soma_cre += cre
    contador += 1
    
    if cre < menor_cre:
        menor_cre = cre
        matricula_menor = matricula

media = soma_cre / contador

print(matricula_menor)
print(f"{media:.2f}")