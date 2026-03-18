def verify(a,b) -> bool:
	if b == 1 or b == 0 or a < b:
		return False
	elif a == b:
		return True
	while a != 1:
		if a % b != 0:
			return False
		a //= b
	return True
while True:
	try:
		a,b = map(int,input().split())
	except:
		break
	if verify(a,b):
		while a != 1:
			print(a,end = " ")
			a//=b
		print(1)
	else:
		print("Boring!")