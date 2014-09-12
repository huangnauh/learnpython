def test():
	print {k:v for k,v in globals().items() if k !="__builtins__"}
test()