hour = int(input("Enter hour: "))
minute = int(input("Enter minute: "))

hour = hour % 12

hour_angle = hour * 30 + minute * 0.5
minute_angle = minute * 6

difference = abs(hour_angle - minute_angle)

if difference > 180:
    difference = 360 - difference

print("Smaller angle =", difference, "degrees")
