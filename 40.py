balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))

minimum_balance = 500

if amount <= 0:
    print("Invalid withdrawal amount")
elif amount > balance:
    print("Insufficient balance")
elif balance - amount < minimum_balance:
    print("Withdrawal rejected: minimum balance must be maintained")
else:
    balance = balance - amount
    print("Withdrawal successful")
    print("Remaining balance =", balance)
