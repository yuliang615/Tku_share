t = int(input())
for _ in range (t):
	inp = list(map(int,input().split()))
	n = inp[0]
	arr = inp[1:n+1]
	arr.sort()
	half = n // 2
	pivot = arr[half]
	ans = 0
	for i in range (n):
		ans += abs(arr[i] - pivot)
	print(ans)