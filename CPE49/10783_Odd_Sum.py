n = int(input())
for i in range(n):
    start = int(input())
    end = int(input())
    total = 0
    for j in range(start, end + 1):
        if j % 2: total += j
    print("Case ", i + 1, ": ", total, sep="")
