def digit(n):
    return str(n)[-1]

def tens(n):
    return str(n)[-2]

def hundreds(n):
    return str(n)[-3]

a = int(input("Enter a number (0 to 9999): "))
print("Digit place is %s." % digit(a))
print("Tens place is %s." % tens(a))
print("Hundreds place is %s." % hundreds(a))