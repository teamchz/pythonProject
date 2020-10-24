a = int(input())


def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

if sum_digits(a) % 9 == 0:
    print("Yes", sum_digits(a))

else:
    print("No", sum_digits(a) % 9)