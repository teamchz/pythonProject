word = input().lower()
box = []

for i in range(len(word)-1):
    box.append(word[i] + word[i+1])

box = list(set(box))
box.sort()
for i in box:
    print(i)