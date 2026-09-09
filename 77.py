def print_pattern(n, current=1):
    if current <= n:
        print(current, end=" ")
        print_pattern(n, current + 1)
    
    if current <= n:
        print(current, end=" ")

n = int(input("Enter n: "))
print_pattern(n)
print()
