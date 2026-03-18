n = int(input())
mp = {}
for _ in range(n):
    arr = input().split()
    mp[arr[0]] = mp.get(arr[0], 0) + 1
ans = list(mp.items())
ans.sort()
for st, freq in ans:    print(st, freq)

