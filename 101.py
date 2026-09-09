n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    spaces = " " * (n - i)
    for j in range(i):
        ch = chr(65 + j)
        print(ch, end=" ")
    print()
