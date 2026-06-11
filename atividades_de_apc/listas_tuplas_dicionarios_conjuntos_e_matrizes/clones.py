from collections import Counter

while True:
    linha = input().strip()
    if linha == "":
        continue  

    n, m = map(int, linha.split())
    if n == 0 and m == 0:
        break 
    
    seqs = []
    for _ in range(n):
        seq = input().strip()
        seqs.append(seq)

    freq = Counter(seqs)
    counts = [0] * (n + 1)
    for qtd in freq.values():
        counts[qtd] += 1

    for i in range(1, n + 1):
        print(counts[i])