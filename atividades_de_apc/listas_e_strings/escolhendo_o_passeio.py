def ganhador():
    if cinema > boliche:
        print("CINEMA")
    elif cinema < boliche:
        print("BOLICHE")
    else:
        print("EMPATE")

cinema = 0
boliche = 0

for i in range(7):
    escolha = input()
    escolha_maisculo = escolha.upper()
    if escolha_maisculo == "CINEMA":
        cinema += 1
    elif escolha_maisculo == "BOLICHE": 
        boliche += 1

ganhador()