try:
    hour = int(input("Enter number of hours: "))
    minute = int(input("Enter number of minute: "))
except:
    print("Input Error!")
    quit()

mix_minute = (hour * 60) + minute

if mix_minute <= 15:
    print("No charge, thanks.")

elif mix_minute < 120:
    print("Total amount due is 20 Bahts.")

else:
    extra = ((hour - 2) * 10) + 20
    print("Total amount due is %d Bahts." % extra)
