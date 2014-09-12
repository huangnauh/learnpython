import io,sys
file = "E:/code/huang/b/learnpy/hello.txt"
f = open(file,"r")
i = io.TextIOWrapper(f.detach(),encoding="utf-8")
print(i.read())
