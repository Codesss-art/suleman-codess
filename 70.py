def is_perfect_number(n):
    if n <= 0:
        return False
    
    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i
    
    return divisor_sum == n

n = int(input("Enter a number: "))
if is_perfect_number(n):
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")
