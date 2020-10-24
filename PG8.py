a = int(input("Enter height: "))

for i in range(a):
    if i == 0:
        print(" " * (a*2-2) + "1")

    else:
        print(" " * ((a*2)-((i+1)*2))
              + "1"
              + " " * (i + (i*3 - 1))
              + "1")