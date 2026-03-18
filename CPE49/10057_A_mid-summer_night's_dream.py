while True:
    try:
        n = int(input())
    except:
        break
    arr = []
    for _ in range(n):
        temp = int(input())
        arr.append(temp)
    arr.sort()
    half1 = arr[len(arr) // 2]
    if len(arr) % 2:
        half2 = half1
    else:
        half2 = arr[(len(arr) // 2) - 1]
    ans = sum(abs(half1 - i) for i in arr)
    count = 0
    for i in arr:
        if i <= half1 and i >= half2:
            count += 1
    print(min(half1, half2), count, half1 - half2 + 1)
