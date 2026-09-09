n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    ch = chr(64 + i)
    for j in range(i):
        print(ch, end=" ")
    print()
