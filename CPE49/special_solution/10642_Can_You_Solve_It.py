n = int(input())
for a in range (n):
	print("Case ",a+1,": ",sep = "",end = "")
	x1,y1,x2,y2 = map(int,input().split())
	a = ((x1 + y1) * (x1 + y1 + 1) // 2) + x1
	b = ((x2 + y2) * (x2 + y2 + 1) // 2) + x2
	print(b - a)