import sys
def main():
    input_all = sys.stdin.read().splitlines()
    it = iter(input_all)
    while True:
        try:
            x = int(next(it))
            arr = list(map(int, next(it).split()))
        except:
            break
        n = len(arr)
        ans = 0
        # n = 2 first is 1
        output = []
        if n == 1:
            print(0)
            continue
        res = arr[0] * (n - 1)
        for i in range(1, n - 1):
            y = (n - i - 1)
            res = res * x + arr[i] * y
        output.append(str(res))
        print("\n".join(output))


main()
