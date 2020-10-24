def factorial(x):
    c = 1
    for i in range(x):
        c *= i + 1
    return c


a = int(input("Enter a number: "))

if a < 0:
    print("Invalid input, program terminates.")
else:
    if a == 0:
        print("0! = 1 = 1")
    elif a == 1:
        print("0! = 1 = 1")
        print("1! = 1 = 1")

    else:
        print("0! = 1 = 1")
        print("1! = 1 = 1")

        for i in range(a-1):
            print("%d! = " % (i + 2), end="")
            for j in range(i+2):
                if j == i+1:
                    print("1 =", factorial(j + 1))
                    break
                print((i + 2) - j, end=" x ")
