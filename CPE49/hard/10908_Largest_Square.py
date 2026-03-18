import sys


def valid(r, c, n, m):
    if r < 0 or c < 0 or r > n - 1 or c > m - 1: return False
    return True


way = [(1, 0), (0, 1), (-1, 0), (0, -1)]
input_all = sys.stdin.read().splitlines()
it = iter(input_all)
t = int(next(it))
for _ in range(t):
    arr = []
    query = []
    n, m, l = map(int, next(it).split())
    print(n, m, l)
    for _ in range(n):
        arr.append(next(it))
    for _ in range(l):
        query.append(tuple(map(int, next(it).split())))
    for i in range(l):
        r, c = query[i]
        current_size = 1
        current_char = arr[r][c]
        ive = True
        d = 1
        while (ive):
            d += 2
            point_r = r - (d // 2)
            point_c = c - (d // 2)
            for k in range(4):
                for j in range(0, d - 1):
                    point_r += way[k][0]
                    point_c += way[k][1]
                    if (not valid(point_r, point_c, n, m) or arr[point_r][point_c] != current_char):
                        ive = False
                        break
                if not ive: break
        d -= 2
        print(d)



