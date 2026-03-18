while True:
	a,b = input().split()
	if(a == "0" and b == "0") : break
	a = '0' + a
	b = '0' + b
	#print(a,b)
	if len(a) < len(b) : a,b = b,a
	while len(a) != len(b) : b = '0' + b
	ans = 0
	carry = False
	for i in range (len(a) - 1,-1,-1):
		if int(a[i]) + int(b[i]) + int(carry) >= 10:
			carry = True
			ans += 1
		else:
		 	carry = False
	if ans > 0 :
		if ans == 1:
			print(ans," carry operation.",sep = "")
		else:
			print(ans," carry operations.",sep = "")
	else : print("No carry operation.")