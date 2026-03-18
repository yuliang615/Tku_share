n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if a < b or ((a + b) % 2):
        print("impossible")
        continue
    print((a + b) // 2, end=" ")
    c = (a - ((a + b) // 2))
    print(c)
