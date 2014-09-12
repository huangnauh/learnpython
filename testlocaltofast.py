import ctypes
import inspect

y = 0

def f():
    frame = inspect.currentframe()
    x = 1
    locals()["x"] = 10
    ctypes.pythonapi.PyFrame_LocalsToFast(ctypes.py_object(frame), 0)
    print "x =", x
    locals()["x"] = 100
    locals()["y"] = 20
    ctypes.pythonapi.PyFrame_LocalsToFast(ctypes.py_object(frame), 0)
    print "x =", x, ", y =", y

f()