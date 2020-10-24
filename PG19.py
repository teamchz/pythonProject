import time

"""
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

print("fibo(%d) = %d" % (n, fibo(n)))
"""

t0 = time.time()
def fibo(n):
    a = 0
    b = 1

    if n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b


n = int(input("Enter n: "))
print("fibo(%d) = %d" % (n, fibo(n)))
print(time.time() - t0)