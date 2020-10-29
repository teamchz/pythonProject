word = input()
b = []
count = 0
while True:
    b.append(input())
    if "0" in b:
        b.remove("0")
        break
b = set(b)
b = list(b)

for i in range(len(word)):
    for j in range(len(b)):
        if b[j] == word[i]:
            count += 1

print("%d/%d" % (count, len(word)))
