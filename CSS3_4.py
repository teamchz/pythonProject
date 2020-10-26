def check(a, b):
    list_a = list(map(str, a))
    word_a = "".join(list_a)
    list_b = list(map(str, b))
    word_b = "".join(list_b)
    if word_b in word_a:
        return True
    else:
        return False


print(check([2, 4, 3, 5, 7], [4, 3, 5]))

