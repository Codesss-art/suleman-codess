n = int(input("Enter a number: "))

count = 0

while n > 0:
    count += n & 1
    n = n >> 1

print("Number of set bits =", count)
