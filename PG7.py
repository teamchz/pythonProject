minute = float(input("Minutes before due: "))
temp = float(input("Temperature: "))
rain = input("Is it raining (y/n)? ").upper()

hour = minute / 60
day = hour / 24
total = int("%.0f" % day)

print(total, "days before due.")

if total < 2:
    print("I will do the assignment.")

elif 2 <= total <= 5:
    if temp > 40 or (temp > 25 and rain == "Y"):
        print("I will not do the assignment.")
    else:
        print("I will do the assignment.")

elif total > 5:
    print("I will not do the assignment.")
