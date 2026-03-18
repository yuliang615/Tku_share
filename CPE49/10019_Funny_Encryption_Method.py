garb = input()
while True:
    try:
        n = int(input())
    except:
        break
    temp = n
    ans_dex = 0
    while temp > 0:
        if temp % 2:
            ans_dex += 1
        temp //= 2
    print(ans_dex, " ", end="", sep="")
    s = str(n)
    ans_hex = 0
    for i, v in enumerate(s):
        val = int(v)
        while val > 0:
            if val % 2:
                ans_hex += 1
            val //= 2
    print(ans_hex, "", sep="")
