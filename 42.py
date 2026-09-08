marks = float(input("Enter marks percentage: "))
attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter family income: "))

if marks >= 75 and attendance >= 75 and income <= 300000:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")
