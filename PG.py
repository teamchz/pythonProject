a = str(input("Enter your buffet choice: "))
if a == "Korean" or a == "Japanese":
    b = str(input("Is today Wednesday (yes/no)? "))
    Korean = 1500
    Japanese = 1000
    lodrakaKorea = 1500*0.85
    lodrakaJapanese = 1000*0.85
    if a == "Korean" and b == "no":
        print("Your payment is %.2f Baht."% (Korean))
    elif a == "Korean" and b == "yes":
        print("Your payment is %.2f Baht."% (lodrakaKorea))
    elif a == "Japanese" and b == "no":
        print("Your payment is %.2f Baht." % (Japanese))
    elif a == "Japanese" and b == "yes":
        print("Your payment is %.2f Baht."% (lodrakaJapanese))

elif a != "Korean" or a != "Japanese":
    print("Sorry, there is no", a, "buffet.")
    quit()