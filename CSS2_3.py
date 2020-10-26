# User input
r = float(input("Enter Interest rate: "))
n = int(input("Enter Compounding: "))
print()

# Create row Period: 1 - 10 %
row = [x for x in range(1, 11)]
print("{:<10}".format("Period"), end="")
for i in row:
    print("{:<10}".format(str(i)+"%"), end="")
print()

# Create each column and calculate
for i in range(n):
    print("{:<10}".format(i+1), end="")
    for j in range(10):
        print("{:<10}".format("%4.3f" % (1 + (j+1) * 0.01)**(i+1)), end="")
    print()
