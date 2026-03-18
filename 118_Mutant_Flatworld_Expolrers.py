import sys
input_all = sys.stdin.read().splitlines()
it = iter(input_all)
right_x,right_y = map(int,next(it).split())
way = [(0,1),(1,0),(0,-1),(-1,0)]
way_map = ('N','E','S','W')
dict = {}
dict['N'] = 0
dict['E'] = 1
dict['S'] = 2
dict['W'] = 3
scent = {}
while True:
	try:
		x,y,pos = next(it).split()
		x = int(x)
		y = int(y)
		s = next(it)
	except:
		break
	pos_int = dict[pos]
	lost = False
	for char in s:
		if char == 'R':
			pos_int = (pos_int + 1) % 4
		elif char == 'L':
			pos_int = (pos_int - 1 + 4) % 4
		else:
			if (x + way[pos_int][0] > right_x or x + way[pos_int][0] < 0 or y+way[pos_int][1] > right_y or y + way[pos_int][1] < 0 ):
				if scent.get((x,y),False) == False:
					scent[(x,y)] = True
					print(f"{x} {y} {way_map[pos_int]} LOST")
					lost = True
					break
				else :
					continue
			else:
				x += way[pos_int][0]
				y += way[pos_int][1]
	if not lost : print(f"{x} {y} {way_map[pos_int]}")