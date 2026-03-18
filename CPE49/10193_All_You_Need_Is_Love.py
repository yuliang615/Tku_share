import math
n = int(input())
for i in range(n):
	print("Pair #",i+1,": ",sep = "",end = "")
	a = int(input(),2)
	b = int(input(),2)
	if(math.gcd(a,b) == 1): print("Love is not all you need!")
	else : print("All you need is love!")