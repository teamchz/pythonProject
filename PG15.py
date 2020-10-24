def check_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            return True
    if n == 2:
        return True


k = int(input("Enter number: "))
if check_prime(k):
    print(k, "is a prime number.")
else:
    print(k, "is not a prime number.")