def mkTree(w):
	i = 1
	try: 
		while tree[i] != w:
			if tree[i] > w:
				i = i*2
			else:
				i = i*2+1
	except KeyError:
		tree[i] = w

src = "yuoteavpxqgrlsdhwfjkzi_cmbn"
tree = {}
for w in src:
	mkTree(w)

path = "DLLDLDLLLLLDLLLLRLDLLDLDLLLRRDLLLLRDLLLLLDLLRLRRRDLLLDLLLDLLLLLDLLRDLLLRRLDLLLDLLLLLDLLLRLDLLDLLRLRRDLLLDLLRLRRRDLLRDLLLLLDLLLRLDLLDLLRLRRDLLLLLDLLRDLLLRRLDLLLDLLLLLDLLRDLLRLRRDLLLDLLLDLLRLRRRDLLLLLDLLLLRLDLLLRRLRRDDLLLRRDLLLRRLRDLLLRLDLRRDDLLLRLDLLLRRRDLLRLRRRDLRRLD"
i = 1
for p in path:
	if p == 'D':
		print(tree[i], end='')
		i = 1
	if p == 'R':
		i = i*2+1
	if p == 'L':
		i = i*2
