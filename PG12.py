a = int(input("Enter a number: "))
b = a
if 0 < a <= 26:

    for i in range(a-1):
        for j in range(i+1):
            print(chr(ord('A') + j), end="")
        print("")

    for i in range(a):
        for j in range(b):
            print(chr(ord('A') + j), end="")
        b -= 1
        print("")

else:
    print("Invalid input, program terminates.")