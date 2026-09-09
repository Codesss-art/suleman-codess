n = int(input("Enter size: "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        elif abs(i - n // 2) + abs(j - n // 2) == n // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
