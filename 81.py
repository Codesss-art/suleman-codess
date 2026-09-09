n = int(input("Enter number of rows: "))

for i in range(n, 0, -1):
    spaces = " " * (n - i)
    stars = "*" * i
    print(spaces + stars)
