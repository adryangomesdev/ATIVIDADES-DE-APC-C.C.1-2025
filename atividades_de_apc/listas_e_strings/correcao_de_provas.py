gabarito = input()
notas = []        
aprovados = 0     
total_alunos = 0 

while True:
    linha = input().split()
    numero = int(linha[0])
    if numero == 9999:
        break

    resposta = ''.join(linha[1:]).strip()

    nota = sum(1 for i in range(10) if i < len(resposta) and resposta[i] == gabarito[i])
    notas.append(nota)

    print(f"{numero} {nota:.1f}")

    if nota >= 6:
        aprovados += 1
    total_alunos += 1

if total_alunos == 0:
    print("0.0%")
    print("0.0")
else:
    percentual = (aprovados / total_alunos) * 100
    print(f"{percentual:.1f}%")
    mais_frequente = max(set(notas), key=notas.count)
    print(f"{mais_frequente:.1f}")