def reverse(x):
    if len(word) < 4:
        return x
    else:
        return x[::-1]


word = input("Enter word: ")
print(reverse(word))
