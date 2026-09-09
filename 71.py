n = int(input("Enter decimal number: "))

binary = ""
temp = n

if n == 0:
    binary = "0"
else:
    while temp > 0:
        binary = str(temp % 2) + binary
        temp = temp // 2

print(f"Binary: {binary}")
