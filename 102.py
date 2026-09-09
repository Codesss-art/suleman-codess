n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    spaces = " " * (n - i)
    chars = " ".join(chr(65 + j) for j in range(i))
    print(spaces + chars)
