while True:
	try:
		n = int(input())
	except:
		break
	temp = n
	while temp > 2:
		n += temp // 3
		tmpa = temp % 3
		temp //= 3
		temp += tmpa
	if temp == 2: n+=1
	print(n)



# while True:
# 	try:
# 		n = int(input())
# 	except:
# 		break
# 	print(int((n * 3) / 2))