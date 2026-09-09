n = int(input("Enter number of rows: "))

for i in range(n):
    for j in range(i + 1):
        ch = chr(65 + j)
        print(ch, end=" ")
    print()
