def progress(n):
    global money
    if n == 0:
        return money
    else:
        return progress(n-1) * 1.05


money = 10000
print(progress(30))
