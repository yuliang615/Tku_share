import sys
from math import fmod
input_all = sys.stdin.read().splitlines()
it = iter(input_all)
while True:
	n,m = map(int,next(it).split())
	print(n,m)
	if n == 0 and m == 0:
		break
	arr = []
	for _ in range(n):
		arr.append(int(next(it)))
	arr.sort(key = lambda x:(fmod(x,m),-(x%2),-x if x%2 else x))
	output = []
	for val in arr:
		output.append(f"{val}")
	print("\n".join(output))