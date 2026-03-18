start = False
while True:
	try:
		s = input()
		for i in range(len(s)):
			if s[i] == '"':
				if start:
					start = False
					print("''",end = "")
				else:
					start = True
					print("``",end = "")
			else:
				print(s[i],end = "")
		print()
	except:
		break