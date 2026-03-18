while True:
    start, end = map(int, input().split());
    if not start and not end:
        break;
    is_square = [False] * 100001
    for i in range(1, 1000):
        if i * i <= 100000:
            is_square[i * i] = True
    count = 0
    for i in range(start, end + 1):
        if is_square[i]:
            count = count + 1
    print(count)

