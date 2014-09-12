import subprocess  

print(subprocess.PIPE)
p = subprocess.Popen(["E:/python34/python.exe",'-u','cgi101.py'], stdin = subprocess.PIPE,stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = False) 

#print(p.stdout.read())

stdoutdata, stderrdata = p.communicate(b"huanglibo")
print(stdoutdata)