while True:
    s = input()
    if int(s) == 0: break
    print(s, end=" ")
    even = 0
    odd = 0
    even = sum(int(i) for index, i in enumerate(s) if index % 2 == 0)
    odd = sum(int(i) for index, i in enumerate(s) if index % 2 == 1)
    if abs(even - odd) % 11 == 0:
        print("is a multiple of 11.")
    else:
        print("is not a multiple of 11.")
