src = '0CA  70  93 0C8    6  7F  23 0A1 0E0  48  2A  39 0AE  54 0F2  79 0F2  84  8B    5 0A2  52  19  29 0C4  54 0AA 0F0 0CA    0'
words = src.split(' ')

i = 0
for w in words:
	if w != '':
		for c in range(32,127):
			if( (((i^c) << ((i^9)&3) | (i^c) >> (8-((i^9)&3)))+8)&0xff == int(w, 16)):
				print chr(c)
		i = i +1


