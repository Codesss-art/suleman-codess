n = int(input("Enter number of rows: "))

for i in range(n):
    for j in range(n):
        if (i + j) % (n - 1) == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
