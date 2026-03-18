t = int(input())
for a in range(t):
    print("Test #", a + 1, ": ", sep="", end="")
    arr = list(input().split())
    n = int(arr[2])
    ans = []
    for _ in range(n):
        temp = list(map(int, input().split()))
        for i, val in enumerate(temp):
            ans.append(val)
    if ans != ans[::-1] or any(x < 0 for x in ans):
        print("Non-symmetric.")
        continue

    print("Symmetric.")

