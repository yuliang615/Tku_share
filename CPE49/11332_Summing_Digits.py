def cac(s:str) -> None:
	total = 0
	n = len(s)
	if n == 1:
		print(s)
		return
	for i in range(n):
		total += int(s[i])
	return cac(str(total))

while True:
	n = input()
	if int(n) == 0:
		break
	cac(n)