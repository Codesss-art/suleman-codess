def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def ncr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

n = int(input("Enter number of rows: "))

for i in range(n):
    for j in range(i + 1):
        print(ncr(i, j), end=" ")
    print()
