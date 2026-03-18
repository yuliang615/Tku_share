import sys

input_data = sys.stdin.read().splitlines()
it = iter(input_data)
line = next(it)
t = int(line)
next(it)
for _ in range(t):
    arr = []
    dict = {}
    while True:
        try:
            temp = next(it)
            if temp == "": break
        except:
            break
        arr.append(temp)
        dict[temp] = dict.get(temp, 0) + 1
    n = int(len(arr))
    ans = []
    for i, value in dict.items():
        ans.append((i, value / n * 100))
    ans.sort()
    output = []
    for i, value in ans:
        output.append(f"{i} {value:.4f}")
    print("\n".join(output))
    if _ != t - 1:
        print()

