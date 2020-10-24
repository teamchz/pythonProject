def tax_calculator(x):
    if x <= 150000:
        print("Hurray, tax exempted.")
        exit(0)

    elif 150001 <= x <= 300000:
        process = (x - 150000) * 0.05

    elif 300001 <= x <= 500000:
        process = (x - 300000) * 0.1 + 7500

    elif 500001 <= x <= 750000:
        process = (x - 500000) * 0.15 + 27500

    elif 750001 <= x <= 1000000:
        process = (x - 750000) * 0.2 + 65000

    elif 1000001 <= x <= 2000000:
        process = (x - 1000000) * 0.25 + 115000

    elif 2000001 <= x <= 5000000:
        process = (x - 2000000) * 0.3 + 365000

    else:
        process = (x - 5000000) * 0.5 + 1265000

    print("Your tax is: %.2f Baht" % process)


income = int(input("Enter your income: "))
tax_calculator(income)


