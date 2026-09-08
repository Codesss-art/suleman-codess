n = int(input("Enter a number: "))

seen = set()

while n != 1 and n not in seen:
    seen.add(n)

    total = 0

    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10

    n = total

if n == 1:
    print("Happy number")
else:
    print("Not a happy number")
