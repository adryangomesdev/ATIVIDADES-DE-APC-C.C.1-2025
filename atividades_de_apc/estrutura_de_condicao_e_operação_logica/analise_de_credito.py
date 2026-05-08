s = float(input())
e = float(input())

if e >= (s * 30 / 100):
    print(f"{(0):.2f}")
elif e < (s * 30 / 100):
    print(f"{((s * 30 / 100) - e):.2f}")