def cac(arr) -> None:
	n = len(arr)
	count = 0
	for i in range (n - 1,-1,-1):
		for j in range (0,i):
			if arr[j] > arr[j+1] :
				count += 1
				arr[j] ,arr[j+1] = arr[j+1] , arr[j]
	print("Optimal train swapping takes ",count," swaps.",sep = "")
t = int(input())
for i in range(t):
	n = int(input())
	arr = input().split()
	for j in range (len(arr)):
		arr[j] = int(arr[j])
	cac(arr)