a = input()
count = []
box = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for i in range(len(a)):
    if a[i] not in box:
        count.append(a[i])
print("".join(count))

