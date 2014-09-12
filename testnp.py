#
#
import time
import numpy as np
import math
#
x = [i * 0.001 for i in xrange(1000000)]
start = time.time()
for i,t in enumerate(x):
	x[i] = math.sin(t)
print("math:",time.time()-start)

x = [i * 0.001 for i in xrange(1000000)]
start = time.time()
for i,t in enumerate(x):
	x[i] = np.sin(t)
print("np:",time.time()-start)