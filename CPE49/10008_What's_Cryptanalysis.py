n = int(input())
mp = {}
def cac(s):
    for ch in s:
        if ch.islower():
            ch = ch.upper()
        if ch.isalpha():
            if ch in mp:
                mp[ch] += 1
            else:
                mp[ch] = 1


def cmp(p):
    return (-p[1], p[0])


for _ in range(n):
    s = input()
    cac(s)
    ans = list(mp.items())
    ans.sort(key=cmp)
for ch, count in ans:
    print(ch, count)