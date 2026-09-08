hour = int(input("Enter hour (0-23): "))

if 5 <= hour < 12:
    print("Morning")
elif 12 <= hour < 17:
    print("Afternoon")
elif 17 <= hour < 21:
    print("Evening")
elif 21 <= hour <= 23 or 0 <= hour < 5:
    print("Night")
else:
    print("Invalid hour")
