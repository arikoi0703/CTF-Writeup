#caculate cuberoot(num)

def cuberoot(num):
	root = 1
	i = 1
	while root**3 <= num:
		root = root * 10
	root = root / 10
	i = root
	while i > 0:
		while root**3 <= num:
			root = root + i
		root = root - i
		i = i / 10
	if root ** 3 == num:
		print root
		return True
	return False
	
i = input('input: ')
cuberoot(i)


