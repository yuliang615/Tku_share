while True:
    try:
        iss = list(map(int, input().split()))
    except:
        break
    n = int(iss[0])
    arr = iss[1:]
    temp = []
    for i in range(1, n):
        temp.append(abs(arr[i] - arr[i - 1]))
    temp.sort()
    jolly = True
    for i in range(0, n - 1):
        if temp[i] != i + 1:
            print("Not jolly")
            jolly = False
            break
    if jolly:
        print("Jolly")

