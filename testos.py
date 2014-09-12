import textwrap
with open('mac.txt','r') as f:
	c= []
	for line in f:
		c.append('-'.join(textwrap.wrap('902B345FB021', width=2)))
	print(c)