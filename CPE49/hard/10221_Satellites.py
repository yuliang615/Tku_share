import sys
import math
input_all = sys.stdin.read().splitlines()
it = iter(input_all)
while True:
	try:
		r,ang,func = next(it).split()
	except:
		break
	r = int(r)
	ang = int(ang)
	r = r + 6440
	ang %= 360
	if ang > 180:ang = 360 - ang
	rag= math.pi * ang / 180.0
	if func == "min" : rag /= 60.0
	print(f"{r*rag:.6f} {2*r*math.sin(rag/2):.6f}")