import sys

input_all = sys.stdin.read().splitlines()
it = iter(input_all)

while True:
    try:
        a = next(it)
        b = list(next(it))
    except:
        break

    ans = []

    for i in a:
        for k in range(len(b)):
            if i == ' ' or b[k] == ' ':
                continue
            if i == b[k]:
                ans.append(i)
                b.pop(k)
                break

    ans = sorted(ans)

    for c in ans:
        print(c, end="")
    print()