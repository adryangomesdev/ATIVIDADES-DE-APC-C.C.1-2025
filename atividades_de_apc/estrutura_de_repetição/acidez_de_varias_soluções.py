while True:
    ph = float(input())
    if 1 <= ph < 7:
        print("ACIDA")
    elif ph > 7:
        print("BASICA")
    elif ph == 7:
        print("NEUTRA")
    elif ph == -1:
        break
    