def check(a, b=['a', 'bc', 123]):
    set_a = set(a)
    set_b = set(b)
    if set_a & set_b:
        return True
    else:
        return False


print(check(['ab', 1, 2, 3, '123']))

