idade = int(input())
jogo = str(input())

if idade >= 21 and jogo == "azar":
    print("Pode entrar!")
elif idade >= 14 and jogo == "mmorpg":
    print("Pode entrar!")
elif idade >= 10 and jogo == "moba":
    print("Pode entrar!")
elif idade >= 0 and jogo == "casual":
    print("Pode entrar!")
elif idade <= 21 and jogo == "azar":
    print("Volte daqui há alguns anos.")
elif idade <= 14 and jogo == "mmorpg":
    print("Volte daqui há alguns anos.")
elif 0 <= idade <= 10 and jogo == "moba":
    print("Volte daqui há alguns anos.")
elif idade <= -1 and jogo == "coisa":
    print("Idade invalida.")
elif idade <= -1 and jogo == "moba":
    print("Idade invalida.")
elif idade >= 21 and jogo == "xadrez":
    print("Jogo invalido.")
elif idade >= 14 and jogo == "xadrez":
    print("Jogo invalido.")
elif idade >= 10 and jogo == "xadrez":
    print("Jogo invalido.")
elif idade >= 0 and jogo == "xadrez":
    print("Jogo invalido.")