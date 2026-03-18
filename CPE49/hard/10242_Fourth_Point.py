import sys
input_all = sys.stdin.read().splitlines()
it = iter(input_all)
while True:
	try:
		x1,y1,x2,y2,x3,y3,x4,y4 = map(float,next(it).split())
	except:
		break
	if x1 == x3 and y1 == y3:
		x = x2 + (x4 - x1)
		y = y2 + (y4 - y1)
	elif x1 == x4 and y1 == y4:
		x = x2+x3-x1
		y = y2+y3-y1
	elif x2 == x3 and y2 == y3:
		x = x1+x4-x2
		y = y1+y4-y2
	elif x2 == x4 and y2 == y4:
		x = x1+x3-x2
		y = y1+y3-y2
	print(f"{x:.3f} {y:.3f}")
'''
//use double
//題目保證給定兩個相鄰
//x1 x2 不可以是相林 x3 x4 不可相鄰 否則會變成長度為0線段
// pair 1 x1 x2
// pair 2 x3 x4
// 需判斷四種
'''