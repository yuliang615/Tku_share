import sys

arr = [[0 for _ in range(32)] for _ in range(13)]
arr[1][1] = 6
arr[2][1] = 2
arr[3][1] = 2
arr[4][1] = 5
arr[5][1] = 0
arr[6][1] = 3
arr[7][1] = 5
arr[8][1] = 1
arr[9][1] = 4
arr[10][1] = 6
arr[11][1] = 2
arr[12][1] = 4
for i in range(1, 13):
    for j in range(2, 32):
        interval = (j - 1)
        arr[i][j] = (arr[i][1] + interval) % 7
input_all = sys.stdin.read().splitlines()
it = iter(input_all)
t = (int(next(it)))
for _ in range(t):
    m, d = map(int, next(it).split())
    if arr[m][d] == 0:
        print("Sunday")
    elif arr[m][d] == 1:
        print("Monday")
    elif arr[m][d] == 2:
        print("Tuesday")
    elif arr[m][d] == 3:
        print("Wednesday")
    elif arr[m][d] == 4:
        print("Thursday")
    elif arr[m][d] == 5:
        print("Friday")
    elif arr[m][d] == 6:
        print("Saturday")
