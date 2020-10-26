word = input("Enter word: ")
character = list(word)
remove_index = [i for i in range(len(word)) if i % 2 != 0]
b = []

for i in range(len(word)):
    if i not in remove_index:
        b.append(word[i])

print(("".join(b)).swapcase())
