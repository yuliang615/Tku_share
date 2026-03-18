import sys
input_all = sys.stdin.read().splitlines()
it = iter(input_all)
t = int(next(it))
for _ in range (t):
	day = int(next(it))
	arr = [False] * (day + 1)
	p = int(next(it))
	for _ in range(p):
		n = int(next(it))
		temp = n
		for i in range(1,day+1):
			if i == temp:
				arr[i] = True
				temp += n
	ans = 0
	for i in range(1,day+1):
		if (i - 1) % 7 != 5 and (i-1) % 7 != 6 and arr[i] == True:
			ans+=1
	print(ans)