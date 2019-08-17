bin = '010,1111,1010,10010,100000,10100,110'.split(',')
f = []
for st in bin:
	if int(st, 2)%5 == 0:
		f.append(st)
print(','.join(f))