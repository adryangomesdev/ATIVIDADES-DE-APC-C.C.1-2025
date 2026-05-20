alunos = int(input())
preco = 2.20

# A cada 3 alunos, paga só 2 escovas
grupos = alunos // 3       # quantidade de trios
resto = alunos % 3         # escovas fora da promoção

total = (grupos * 2 + resto) * preco

print(f"{total:.2f}")
