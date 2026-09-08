n = int(input("Enter a number: "))
k = int(input("Enter the bit position: "))

if n & (1 << k):
    print("Kth bit is SET")
else:
    print("Kth bit is NOT SET")
