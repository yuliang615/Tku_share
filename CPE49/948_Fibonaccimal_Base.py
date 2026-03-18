t = int(input())
arr = []
arr.append(0)
arr.append(1)
for i in range(2, 41):
    arr.append(arr[i - 1] + arr[i - 2])
for _ in range(t):
    n = int(input())
    print(n, " = ", sep="", end="")
    start = False;
    for i in range(40, 1, -1):
        if arr[i] > n:
            if start:
                print("0", end="")
        else:
            n -= arr[i]
            start = True
            print("1", end="")
    print(" (fib)")
