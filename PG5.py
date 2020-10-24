tv = float(input("How many TVs? ")) * 6000
dvd = float(input("How many DVD players? ")) * 1500
audio = float(input("How many Audio Systems? ")) * 3000
total = tv + dvd + audio
discount = total * 0.2

if total >= 24000:
    print("Total price is %.2f baht." % total)
    print("You've got a discount of %.2f baht." % discount)
    print("Your payment is %.2f baht. Thank you!" % (total - discount))

else:
    print("Total price is %.2f baht." % total)
    print("Your payment is %.2f baht. Thank you!" % total)
