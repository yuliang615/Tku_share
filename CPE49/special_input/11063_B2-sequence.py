count = 0
while True:
	try:
		line = input()
		if(line == "") : continue
		n = int(line)
	except:
		break
	count+=1
	print("Case #",count,": ",sep = "",end = "")
	arr = list(map(int,input().split()))
	correct = True
	if any(i <= 0 for i in arr) :
		correct = False
	for i in range(len(arr)):
		for j in range(i + 1,len(arr)):
			if arr[i] >= arr[j]:
				correct = False
				break
	dict = {}
	for i in range(len(arr)):
		for j in range(i,len(arr)):
			if(dict.get(arr[i] + arr[j],0) != 0):
				correct = False
			else: dict[arr[i] + arr[j]] = 1
	if correct:
		print("It is a B2-Sequence.")
	else:
		print("It is not a B2-Sequence.")
	print()