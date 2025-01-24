import random

N = int(input("Anna arvottavien pisteiden määrä: "))

sisalla = 0

for _ in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x ** 2 + y ** 2 < 1:
        sisalla += 1

pi_likiarvo = 4 * sisalla / N

print(f"Piin likiarvo on noin: {pi_likiarvo}")