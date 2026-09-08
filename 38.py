n = int(input("Enter a 3-digit number: "))

original = n

a = n // 100
b = (n // 10) % 10
c = n % 10

sum = a ** 3 + b ** 3 + c ** 3

if sum == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
