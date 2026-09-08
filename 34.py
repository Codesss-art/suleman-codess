import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = b * b - 4 * a * c

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)

    print("Two real roots:")
    print(root1)
    print(root2)

elif d == 0:
    root = -b / (2 * a)
    print("Equal real roots:")
    print(root)

else:
    real = -b / (2 * a)
    imaginary = math.sqrt(-d) / (2 * a)

    print("Imaginary roots:")
    print(real, "+", imaginary, "i")
    print(real, "-", imaginary, "i")
