#rsa
import binascii
c = 0x1afe93e83137e76d2226d97c40512040
d = 31337
n = 0x50618b968b8603e9e870e7d878e866e3

p = c**d % n
print('%x' % c)
print('%x' % p)
flag = str('%x' % p)

for i in range(int(len(flag)/2)):
	key = flag[i*2] + flag[i*2+1]
	#print(key)
	print(binascii.unhexlify('%x' % int(key, 16)))

