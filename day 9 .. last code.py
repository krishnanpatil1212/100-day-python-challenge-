for i in range(3):
    for j in range(7):
        if (j == 1 or j == 5) and i == 0 or \
           (j == 0 or j == 2 or j == 4 or j == 6) and i == 1 or \
           (j >= 1 and j <= 5) and i == 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(3):
    print(" " * (i + 1) + "*" * (5 - 2*i))
