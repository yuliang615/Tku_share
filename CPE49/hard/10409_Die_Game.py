import sys
input_all = sys.stdin.read().splitlines()
it = iter(input_all)
while True:
	n = int(next(it))
	if n == 0 :
		break
	arr = []
	top, north, west, east, south, down = 1, 2, 3, 4, 5, 6
	for _ in range (n):
		arr.append(next(it))
	for way in arr:
		if way == "north":
			temp = top
			top = south
			south = down
			down = north
			north = temp
		elif way == "south":
			temp = top
			top = north
			north = down
			down = south
			south = temp
		elif way == "east":
			temp = top
			top = west
			west = down
			down = east
			east = temp
		else:
			temp = top
			top = east
			east = down
			down = west
			west = temp
	print(top)