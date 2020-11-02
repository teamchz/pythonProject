def decription(x):
    vowels = ['a', 'e', 'i', 'o', 'u']
    i = 0
    result = []
    while i < len(x):
        if x[i] in vowels:
            result.append(x[i])
            i += 3
        else:
            result.append(x[i])
            i += 1
        if i == len(x):
            print("".join(result))


word = input()
decription(word)