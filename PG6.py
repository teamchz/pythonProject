print("---<< Main Menu >>---\n    <B>urger Meal\n    <C>hicken Meal\n    <P>asta Meal")
choice_a = input("Enter your choice: ").upper()

if choice_a == "B":
    print("---<< Burger Sub Menu >>---\n    <R>egular Burger\n    <C>heese Burger\n    <D>ouble Cheese Burger")
    choice_b = input("Enter your choice: ").upper()
    if choice_b == "R":
        print("Your Regular Burger is 60 Baht.")
    elif choice_b == 'C':
        print("Your Cheese Burger is 75 Baht.")
    elif choice_b == "D":
        print("Your Double Cheese Burger is 90 Baht.")
    else:
        print("Invalid sub menu choice.")

elif choice_a == "C":
    print("---<< Chicken Sub Menu >>---\n    <F>ried Chicken\n    <G>rilled Chicken\n    <C>hef's Chicken")
    choice_b = input("Enter your choice: ").upper()
    if choice_b == "F":
        print("Your Fried Chicken is 120 Baht.")
    elif choice_b == 'G':
        print("Your Grilled Chicken is 150 Baht.")
    elif choice_b == "C":
        print("Your Chef's Chicken is 180 Baht.")
    else:
        print("Invalid sub menu choice.")

elif choice_a == "P":
    print("---<< Pasta Sub Menu >>---\n    <S>paghetti de Italiano\n    <L>asagna Supreme\n    <M>acaroni Special")
    choice_b = input("Enter your choice: ").upper()
    if choice_b == "S":
        print("Your Spaghetti de Italiano is 90 Baht.")
    elif choice_b == 'L':
        print("Your Lasagna Supreme is 120 Baht.")
    elif choice_b == "M":
        print("Your Macaroni Special is 100 Baht.")
    else:
        print("Invalid sub menu choice.")

else:
    print("Invalid main menu choice.")
