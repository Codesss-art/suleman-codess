n = int(input("Enter size: "))

for i in range(n):
    for j in range(n):
        dist1 = abs(i - n // 2) + abs(j - n // 4)
        dist2 = abs(i - n // 2) + abs(j - 3 * n // 4)
        dist3 = abs(i - n // 4) + abs(j - n // 2)
        
        if dist1 <= n // 4 or dist2 <= n // 4 or (i > n // 2 and abs(j - n // 2) <= i - n // 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
