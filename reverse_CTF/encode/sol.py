code = 44099282625849925

flag = ''
while code > 0:
	c = code%26
	flag = flag + chr(ord('A')+c)
	code = code // 26
print flag[::-1]
