import math


def verify(n) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def cac(n) -> None:
    tmp = n
    if verify(n):
        n2 = 0
        while tmp > 0:
            n2 *= 10
            n2 += (tmp % 10)
            tmp //= 10
        if verify(n2) and n2 != n:
            print(n, "is emirp.")
        else:
            print(n, "is prime.")
    else:
        print(n, "is not prime.")


while True:
    try:
        n = int(input())
        cac(n)
    except:
        break
