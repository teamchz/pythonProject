a = int(input()) ** 2
count = 0

for i in range(a):
    for j in range(a):
        if (j**2) + (i**2) == a:
            count += 1

if a == 1:
    print(0)
    quit()
print(int(count / 2 - 1))
