arr = []
max_s_size = -1
def cac(arr):
	for i in range(max_s_size):
		for j in range(len(arr)-1,-1,-1):
			print(arr[j][i],end = "");
		print()
while True:
	try:
		s = input()
		arr.append(s)
		max_s_size = max(max_s_size,len(s))
	except:
		break
	for i in range(len(arr)):
		while (len(arr[i]) != max_s_size):
			arr[i] += ' '
cac(arr)