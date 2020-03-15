src = 'zGs7@ABp"sIp/3bn@-:A-G]CllNNK'

for i in range(len(src)):
	for c in range(32,255):
		if src[i] == chr((c+13)%95+32):
			print chr(c)
			break
