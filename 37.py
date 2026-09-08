x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))

if x > 0 and y > 0:
    print("First quadrant")
elif x < 0 and y > 0:
    print("Second quadrant")
elif x < 0 and y < 0:
    print("Third quadrant")
elif x > 0 and y < 0:
    print("Fourth quadrant")
elif x == 0 and y == 0:
    print("Origin")
elif x == 0:
    print("On Y-axis")
else:
    print("On X-axis")
