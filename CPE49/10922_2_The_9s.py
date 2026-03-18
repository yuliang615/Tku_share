while True:
    n = input()
    if int(n) == 0: break
    print(n, sep="", end="")
    count = 1
    temp = sum(int(c) for c in n)
    while (temp >= 10):
        if (temp % 9) == 0:
            count += 1
            temp = sum(int(c) for c in str(temp))
        else:
            count = 0
            break

    if count >= 1:
        print(" is a multiple of 9 and has 9-degree ", count, ".", sep="")
    else:
        print(" is not a multiple of 9.")