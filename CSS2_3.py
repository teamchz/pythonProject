# User input
r = float(input("Enter Interest rate: "))
n = int(input("Enter Compounding: "))
print()

# Create row Period: 1 - 10 %
row = [x for x in range(1, 11)]
row.insert(0, "Period")
for i in row:
    print(i, end="\t\t")
print()

# Create each column and calculate
for i in range(n):
    print(i+1, end="\t\t\t")
    for j in range(10):
        print("%4.3f" % (1 + (j+1) * 0.01)**(i+1), end="\t")
    print()