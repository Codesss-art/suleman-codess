binary = input("Enter binary number: ")

decimal = 0
power = 0

for i in range(len(binary) - 1, -1, -1):
    digit = int(binary[i])
    decimal = decimal + digit * (2 ** power)
    power += 1

print(f"Decimal: {decimal}")
