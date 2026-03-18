def cmp(p):
    return (p[1], -p[0])


def cac(s):
    mp = {}
    for ch in s:
        mp[ord(ch)] = mp.get(ord(ch), 0) + 1
    ans = list(mp.items())
    ans.sort(key=cmp)
    for ch, freq in ans:
        print(ch, freq)


start = 0
while True:
    try:
        s = input()
        if start: print("")
        cac(s)
        start += 1
    except:
        break