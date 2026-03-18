import sys

input_all = sys.stdin.read().splitlines()
it = iter(input_all)
while True:
    n = int(next(it))
    if n == 0:
        break
    print("The parity of ", sep="", end="")
    print(bin(n)[2:], " is ", sep="", end="")
    print(sum(int(i) for i in bin(n)[2:]), sep="", end="")
    print(" (mod 2).")


