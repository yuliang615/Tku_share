dict = {}
for i in range(0, 10): dict[str(i)] = i
for i, v in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    dict[v] = i + 10
for i, v in enumerate("abcdefghijklmnopqrstuvwxyz"):
    dict[v] = i + 36
while True:
    try:
        s = input()
    except:
        break
    if len(s) == 1 and not s.isalpha() and (int(s) == 0 or int(s) == 1):
        print(2)
        continue
    temp = 0
    max_num = -1
    for i in s:
        if not i.isalpha() and not i.isdigit(): continue
        temp += dict[i]
        max_num = max(max_num, dict[i])
    ans = 0
    for i in range(1, 62):
        if (temp % i == 0 and i > max_num - 1):
            ans = i
            break
    print(ans + 1 if ans != 0 else "such number is impossible!")

