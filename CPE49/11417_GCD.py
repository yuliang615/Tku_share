import math
while True:
	n = int(input())
	if n == 0:
		break
	G = 0
	for i in range(1,n):
		for j in range (i+1,n+1):
			G += math.gcd(i,j)
	print(G)