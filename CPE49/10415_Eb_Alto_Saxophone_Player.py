import sys
dict = {}
		   #(0,1,2,3,4,5,6,7,8,9,10)
dict['c'] = (0,0,1,1,1,0,0,1,1,1,1)
dict['d'] = (0,0,1,1,1,0,0,1,1,1,0)
dict['e'] = (0,0,1,1,1,0,0,1,1,0,0)
dict['f'] = (0,0,1,1,1,0,0,1,0,0,0)
dict['g'] = (0,0,1,1,1,0,0,0,0,0,0)
dict['a'] = (0,0,1,1,0,0,0,0,0,0,0)
dict['b'] = (0,0,1,0,0,0,0,0,0,0,0)
dict['C'] = (0,0,0,1,0,0,0,0,0,0,0)
dict['D'] = (0,1,1,1,1,0,0,1,1,1,0)
dict['E'] = (0,1,1,1,1,0,0,1,1,0,0)
dict['F'] = (0,1,1,1,1,0,0,1,0,0,0)
dict['G'] = (0,1,1,1,1,0,0,0,0,0,0)
dict['A'] = (0,1,1,1,0,0,0,0,0,0,0)
dict['B'] = (0,1,1,0,0,0,0,0,0,0,0)
input_all = sys.stdin.read().splitlines()
it = iter(input_all)
t = int(next(it))
for _ in range(t):
	stat = [False] * 11
	times = {}
	s = next(it)
	for i,ch in enumerate(s):
		temp = dict[ch]
		for j in range(1,11):
			if temp[j] == 1:
				if stat[j] == True:
					continue
				elif stat[j] == False:
					times[j] = times.get(j,0) + 1
					stat[j] = True
			else:
				stat[j] = False
	for i in range(1,11):
		print(times.get(i,0),end = "")
		if i != 10 : print(" ",end = "")
	print()