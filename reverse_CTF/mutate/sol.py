src = '58 6D 4A 64 56 56 64 52 6F 7C 59 51 1F 7B 4B 5D 63 54 6D 6B 4 47 69 6 6B 66 4C 8 6E 64 61 5A 74 32 3B 1C 2 2A 14 18 25 7A 37 4B 4C 4D 4E 4F 50 51'
words = src.split(' ')
i = 0
for w in words:
	print chr( int(w,16)^(i+32) )
	i = i+1
