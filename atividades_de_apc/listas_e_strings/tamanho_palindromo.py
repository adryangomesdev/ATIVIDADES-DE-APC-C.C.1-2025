def verificar_palindromo(palavra):
    return palavra == palavra[::-1]

palavra = input()

if verificar_palindromo(palavra) == True:
    print("SIM")
    tamanho_substring = len(set(palavra))
    print(tamanho_substring)
else:
    print("NAO")

    