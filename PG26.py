a = input()
if len(a) % 2 == 0:
    for i in range(int(len(a)/2)):
        print(a[i], end="")
        print((a[-(i+1)]), end="")
else:
    for i in range(int(len(a) / 2)):
        print(a[i], end="")
        print((a[-(i + 1)]), end="")
    c = int(len(a)/2 + 1)
    print(a[c-1])
