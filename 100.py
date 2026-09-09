n = int(input("Enter number of rows: "))

for i in range(n, 0, -1):
    for j in range(i):
        ch = chr(65 + j)
        print(ch, end=" ")
    print()
