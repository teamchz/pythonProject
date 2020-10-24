# a = 5
a = int(input())
b = []
c = []
for i in range(a):
    if (i+1) % 2 != 0:
        b.append(-(i+1))
    else:
        c.append(i+1)
print(sum(b) + sum(c))
