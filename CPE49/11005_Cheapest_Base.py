t = int(input())
for j in range(t):
    if j > 0: print()
    print("Case ", j + 1, ":", sep="")
    arr = []
    dict = {}
    for _ in range(4):
        b = list(map(int, input().split()))
        arr.extend(b)
    # print(arr)
    for i in range(0, 36):
        dict[i] = arr[i]
    n = int(input())
    for _ in range(n):
        ans_dict = {}
        m = int(input())
        print("Cheapest base(s) for number ", m, ":", end="", sep="")
        temp = m
        min_cost = 99999999999
        for i in range(2, 37):
            temp = m
            cost = 0
            while temp > 0:
                cost += dict[temp % i]
                temp //= i
            ans_dict[i] = cost
            min_cost = min(min_cost, cost)
        # print(min_cost)
        for key, value in ans_dict.items():
            if value == min_cost: print(" ", key, end="", sep="")
        print()

