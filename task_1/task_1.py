binary = '010,1111,1010,10010,100000,10100,110'.split(',')
for st in binary:
	n = int(st, 2)
	if n%5 == 0:
		print(st)