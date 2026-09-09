n = int(input("Enter size: "))

for i in range(n):
    for j in range(n):
        if i == j or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
