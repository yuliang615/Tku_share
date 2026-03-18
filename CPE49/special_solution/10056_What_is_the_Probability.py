import sys
input_all = sys.stdin.read().splitlines()
it = iter(input_all)
t = int(next(it))
for _ in range (t):
	N,P,I = next(it).split()
	N = int(N)
	P = float(P)
	I = int(I)
	if P == 0:
		print("0.0000")
		continue
	print(f"{(P * pow(1-P,I-1)/(1 - pow(1-P,N))):.4f}")
'''
    a / (1 - R);
'''