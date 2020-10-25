a = input()
if len(a) % 2 != 0:
    left = int(len(a) / 2)
    right = left + 1
    word_left = a[:left]
    word_right = a[right:]
    print(word_left[::-1], end="")
    print(a[left], end="")
    print(word_right[::-1])

else:
    left = int(len(a) / 2)
    word_left = a[:left]
    word_right = a[left:]
    print(word_left[::-1], end="")
    print(word_right[::-1])
