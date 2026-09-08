n = int(input("Enter a number: "))

original = n
n = abs(n)
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

if original < 0:
    reverse = -reverse

print("Reverse =", reverse)
