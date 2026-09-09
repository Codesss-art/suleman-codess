import math

x = float(input("Enter value of x (in radians): "))
n = int(input("Enter number of terms: "))

result = 0

for i in range(n):
    power = 2 * i + 1
    factorial = math.factorial(power)
    term = (x ** power) / factorial
    
    if i % 2 == 0:
        result += term
    else:
        result -= term

print(f"Sum of series: {result}")
print(f"sin({x}) using math.sin: {math.sin(x)}")
