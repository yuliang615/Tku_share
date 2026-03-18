import sys

input_all = sys.stdin.read().splitlines()
it = iter(input_all)


def cac(n):
    if n >= 10000000:
        cac(n // 10000000)
        n %= 10000000
        print(" kuti", sep="", end="")
        if (n): print(" ", sep="", end="")
    if n >= 100000:
        print(n // 100000, " lakh", sep="", end="")
        n %= 100000
        if (n): print(" ", sep="", end="")
    if n >= 1000:
        print(n // 1000, " hajar", sep="", end="")
        n %= 1000
        if (n): print(" ", sep="", end="")
    if n >= 100:
        print(n // 100, " shata", sep="", end="")
        n %= 100
        if (n): print(" ", sep="", end="")
    if n:
        print(n, end="", sep="")


count = 0
while True:
    count += 1
    try:
        n = int(next(it))
    except:
        break
    if n == 0:
        print(f"{count:4d}. 0", end="")
        print()
        continue
    print(f"{count:4d}. ", end="")
    cac(n)
    print()
