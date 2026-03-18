adj = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
def valid(a, b, n, m):
    if a < 0 or b < 0 or a > n - 1 or b > m - 1: return False
    return True
count = 0
while True:
    count += 1
    n, m = map(int, input().split())
    if n == 0 and m == 0: break
    if (count > 1): print()
    print("Field #", count, ":", sep="")
    arr = []
    ans = [['0' for _ in range(m)] for _ in range(n)]
    for _ in range(n):
        s = input()
        arr.append(s)
    for i in range(n):
        for j in range(m):
            if (arr[i][j] == '*'): ans[i][j] = '*'
    for i in range(n):
        for j in range(m):
            if (arr[i][j] == '*'):
                for z in range(8):
                    to_x = i + adj[z][0]
                    to_y = j + adj[z][1]
                    if (valid(to_x, to_y, n, m) and ans[to_x][to_y] != '*'):
                        ans[to_x][to_y] = str(int(ans[to_x][to_y]) + 1)
    for i in range(n):
        for j in range(m):
            print(ans[i][j], sep="", end="")
        print()
