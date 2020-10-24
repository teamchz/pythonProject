age = int(input("Enter your age: "))
income = float(input("Enter your net income: "))

if age < 15 or age > 60:
    print("Invalid age.")

else:
    if 1 <= income <= 30000:
        print("Your negative income tax is %.2f Baht." % (income * 0.2))

    elif 30000 < income <= 79999:
        print("Your negative income tax is %.2f Baht." % (6000 - (income - 30000) * 0.12))

    elif income >= 80000:
        print("Invalid income.")
