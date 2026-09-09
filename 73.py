count = 0
total = 0

while True:
    num = int(input("Enter number (-1 to stop): "))
    if num == -1:
        break
    count += 1
    total += num

if count > 0:
    average = total / count
    print(f"Count: {count}")
    print(f"Average: {average}")
else:
    print("No numbers entered")
