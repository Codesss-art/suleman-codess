choice = input("Enter C for Celsius to Fahrenheit or F for Fahrenheit to Celsius: ")

if choice == "C" or choice == "c":
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9 / 5) + 32
    print("Temperature in Fahrenheit =", f)

elif choice == "F" or choice == "f":
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5 / 9
    print("Temperature in Celsius =", c)

else:
    print("Invalid choice")
