Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import fractions
>>> a = fractions.Fraction(5,4)
>>> a
Fraction(5, 4)
>>> b = fractions.Franction(4,5)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    b = fractions.Franction(4,5)
AttributeError: 'module' object has no attribute 'Franction'
>>> b = fractions.Fraction(4,5)
>>> a * b
Fraction(1, 1)
>>> print(a*b)
1
>>> a.numerator
5
>>> a.denominator
4
>>> a.numerator
5
>>> a.denominator
4
\
>>> float(a)
1.25
>>> a.limit_denominator(8)
Fraction(5, 4)
>>> a.limit_denominator(3)
Fraction(4, 3)
>>> b = fractions.Fraction(3.75)
>>> b
Fraction(15, 4)
>>> x= 3.75
>>> x.as_integer_ratio()
(15, 4)
>>> b = fractions.Fraction(3.75,10)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    b = fractions.Fraction(3.75,10)
  File "E:\Python34\lib\fractions.py", line 163, in __new__
    raise TypeError("both arguments should be "
TypeError: both arguments should be Rational instances
>>> b = fractions.Fraction(3,75)
>>> b = fractions.Fraction(3.75)
>>> b
Fraction(15, 4)
>>> import array
>>> a = array.array('i',[1,2,3,4])
>>> a
array('i', [1, 2, 3, 4])
>>> a+10
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a+10
TypeError: can only append array (not "int") to array
>>> a*2
array('i', [1, 2, 3, 4, 1, 2, 3, 4])
>>> import numpy
>>> ax = numpy.array([1,2,3,4,5])
>>> ax
array([1, 2, 3, 4, 5])
>>> ax+2
array([3, 4, 5, 6, 7])
>>> ax*2
array([ 2,  4,  6,  8, 10])
>>> ay = numpy.array([5,3,2,1])
>>> ay
array([5, 3, 2, 1])
>>> ax+ ay
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    ax+ ay
ValueError: operands could not be broadcast together with shapes (5,) (4,) 
>>> ay = numpy.array([5,3,2,1,0])
>>> ax+ay
array([6, 5, 5, 5, 5])
>>> def foo(x):
	return 2*x**2-2*x+7

>>> f(ax)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    f(ax)
NameError: name 'f' is not defined
>>> foo(ax)
array([ 7, 11, 19, 31, 47])
>>> tok_regex = r'\s*//.*'
>>> tok_cmp = re.compile(tok_regex)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    tok_cmp = re.compile(tok_regex)
NameError: name 're' is not defined
>>> import re
>>> tok_cmp = re.compile(tok_regex)
>>> tok_cmp.match('re=//sfdfd')
>>> tok_cmp.match('//sfdfd')
<_sre.SRE_Match object; span=(0, 7), match='//sfdfd'>
>>> tok_cmp.match('   //sfdfd')
<_sre.SRE_Match object; span=(0, 10), match='   //sfdfd'>
>>> text = '//sadfsfds var aa="//sdfsfsdfds"'
>>> tok_cmp = re.compile(r'(?<!")//*(?=\s*)')
>>> tok_cmp.replace('',text)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    tok_cmp.replace('',text)
AttributeError: '_sre.SRE_Pattern' object has no attribute 'replace'
>>> tok_cmp
re.compile('(?<!")//*(?=\\s*)')
>>> text.replace(r'(?<!")//*(?=\s*)','')
'//sadfsfds var aa="//sdfsfsdfds"'
>>> text
'//sadfsfds var aa="//sdfsfsdfds"'
>>> tok_cmp.match(text)
<_sre.SRE_Match object; span=(0, 2), match='//'>
>>> tok_cmp = re.compile(r'(?<!")//.*(?=\s*)')
>>> tok_cmp.match(text)
<_sre.SRE_Match object; span=(0, 32), match='//sadfsfds var aa="//sdfsfsdfds"'>
>>> tok_cmp = re.compile(r'(?<!")//.*?(?=\s*)')
>>> tok_cmp.match(text)
<_sre.SRE_Match object; span=(0, 2), match='//'>
>>> tok_cmp = re.compile(r'(?<!")//.+?(?=\s*)')
>>> tok_cmp.match(text)
<_sre.SRE_Match object; span=(0, 3), match='//s'>
>>> tok_cmp = re.compile(r'(?<!")//.*?(?=\s+)')
>>> tok_cmp.match(text)
<_sre.SRE_Match object; span=(0, 10), match='//sadfsfds'>
>>> tok_cmp.match(text.10)
SyntaxError: invalid syntax
>>> tok_cmp.match(text,10)
>>> '//sadfsfds var aa="//sdfsfsdfds" //sadfsf'
'//sadfsfds var aa="//sdfsfsdfds" //sadfsf'
>>> tok_cmp.findall(text)
['//sadfsfds']
>>> text
'//sadfsfds var aa="//sdfsfsdfds"'
>>> len(text)
32
>>> text[31]
'"'
>>> text = '//sadfsfds var aa="//sdfsfsdfds" //sadfsf'
>>> len(text)
41
>>> text[40]
'f'
>>> text[41]
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    text[41]
IndexError: string index out of range
>>> '//sadfsfds var aa="//sdfsfsdfds" //sadfsf'.replace(r'(?<!")//.*?(?=\s+)','')
'//sadfsfds var aa="//sdfsfsdfds" //sadfsf'
>>> '//sadfsfds var aa="//sdfsfsdfds" //sadfsf'
'//sadfsfds var aa="//sdfsfsdfds" //sadfsf'
>>> s = '//sadfsfds var aa="//sdfsfsdfds" //sadfsf'.replace(r'(?<!")//.*?(?=\s+)','')
>>> s
'//sadfsfds var aa="//sdfsfsdfds" //sadfsf'
>>> re.sub(r'(?<!")//.*?(?=\s+)','',text)
' var aa="//sdfsfsdfds" //sadfsf'
>>> re.sub(r'(?<!")//.*?\s+','',text)
'var aa="//sdfsfsdfds" //sadfsf'
>>> re.sub(r'(?<!")//.*?\s+','',text)
'var aa="//sdfsfsdfds" //sadfsf'
>>> text = '//sadfsfds var aa="//sdfsfsdfds" //sadfsf '
>>> re.sub(r'(?<!")//.*?\s+','',text)
'var aa="//sdfsfsdfds" '
>>> text = '//sadfsfds var aa="//sdfsfsdfds" aa=""//sadfsf '
>>> re.sub(r'(?<!")//.*?\s+','',text)
'var aa="//sdfsfsdfds" aa=""//sadfsf '
>>> re.sub(r'(?<!=")//.*?\s+','',text)
'var aa="//sdfsfsdfds" aa=""'
>>> re.sub(r'(?<!=\s*?"\s*?)//.*?\s+','',text)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    re.sub(r'(?<!=\s*?"\s*?)//.*?\s+','',text)
  File "E:\Python34\lib\re.py", line 175, in sub
    return _compile(pattern, flags).sub(repl, string, count)
  File "E:\Python34\lib\re.py", line 288, in _compile
    p = sre_compile.compile(pattern, flags)
  File "E:\Python34\lib\sre_compile.py", line 469, in compile
    code = _code(p, flags)
  File "E:\Python34\lib\sre_compile.py", line 454, in _code
    _compile(code, p.data, flags)
  File "E:\Python34\lib\sre_compile.py", line 109, in _compile
    raise error("look-behind requires fixed-width pattern")
sre_constants.error: look-behind requires fixed-width pattern
>>> re.sub(r'(?<!=\s*"\s*)//.*?\s+','',text)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    re.sub(r'(?<!=\s*"\s*)//.*?\s+','',text)
  File "E:\Python34\lib\re.py", line 175, in sub
    return _compile(pattern, flags).sub(repl, string, count)
  File "E:\Python34\lib\re.py", line 288, in _compile
    p = sre_compile.compile(pattern, flags)
  File "E:\Python34\lib\sre_compile.py", line 469, in compile
    code = _code(p, flags)
  File "E:\Python34\lib\sre_compile.py", line 454, in _code
    _compile(code, p.data, flags)
  File "E:\Python34\lib\sre_compile.py", line 109, in _compile
    raise error("look-behind requires fixed-width pattern")
sre_constants.error: look-behind requires fixed-width pattern
>>> re.sub(r'(?<!=")//.*?\s+','',text)
'var aa="//sdfsfsdfds" aa=""'
>>> text
'//sadfsfds var aa="//sdfsfsdfds" aa=""//sadfsf '
>>> text='//sadfsfds var aa="//sdfsfsdfds" aa=""//sadfsf'
>>> re.findall(r'c[a$]','c')
[]
>>> re.findall(r'c[a]','ca')
['ca']
>>> re.findall(r'c$','c')
['c']
>>> re.findall(r'c$','cd')
[]
>>> re.findall(r'c[$]','c')
[]
>>> re.sub(r'((?<!=")//.*?\s+)|((?<!=")//.*)','',text)
'var aa="//sdfsfsdfds" aa=""'
>>> 
>>> text='//sadfsfds'
>>> re.sub(r'((?<!=")//.*?\s+)|((?<!=")//.*)','',text)
''
>>> re.sub(r'(?<!=")//.*?\s+','',text)
'//sadfsfds'
>>> re.sub(r'(?<!=")//\w+','',text)
''
>>> re.sub(r'(?<!=")//\w+','','//sadfsfds var aa="//sdfsfsdfds" aa=""//sadfsf')
' var aa="//sdfsfsdfds" aa=""'
>>> re.sub(r'(?<!=")//\w*\s*','','//sadfsfds var aa="//sdfsfsdfds" aa=""//sadfsf')
'var aa="//sdfsfsdfds" aa=""'
>>> a="dfef="//
KeyboardInterrupt
>>> re.sub(r'(?<!=")//\w*\s*','','//sadf_sfds var aa="//sdfsfsdfds" aa=""//sadfsf')
'var aa="//sdfsfsdfds" aa=""'
>>> re.sub(r'(?<!=")//\w*\s*','','//sadf_1sfds var aa="//sdfsfsdfds" aa=""//sadfsf')
'var aa="//sdfsfsdfds" aa=""'
>>> re.sub(r'(?<!=")//\w*\s*','','//sadf_s*fds var aa="//sdfsfsdfds" aa=""//sadfsf')
'*fds var aa="//sdfsfsdfds" aa=""'
>>> re.sub(r'(?<!=")//\w*\s*','','//sadf_s*fds var aa="//sdfsfsdfds" aa=""//sadfsf')
KeyboardInterrupt
>>> 
KeyboardInterrupt
re.sub(r'(?<!=")//\w*\s*','','//sadf_s*fds var aa="//sdfsfsdfds" aa=""//sadfsf')
>>> re.sub(r'(?<!=")//\w*\s*','','//sadf_s中fds var aa="//sdfsfsdfds" aa=""//sadfsf')
'var aa="//sdfsfsdfds" aa=""'
>>> c = numpy.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]])
>>> c
array([[ 1,  2,  3,  4],
       [ 4,  5,  6,  7],
       [ 7,  8,  9, 10]])
>>> c.dtype
dtype('int32')
>>> b
Fraction(15, 4)
>>> a
array('i', [1, 2, 3, 4])
>>> d = numpy.array([[1, 2, 3, 4])
		
SyntaxError: invalid syntax
>>> d = numpy.array([1, 2, 3, 4])
>>> d
array([1, 2, 3, 4])
>>> d.dtype
dtype('int32')
>>> d.shape
(4,)
>>> c.shape
(3, 4)
>>> c.shape = 4,3
>>> c
array([[ 1,  2,  3],
       [ 4,  4,  5],
       [ 6,  7,  7],
       [ 8,  9, 10]])
>>> d = c.reshape((3,-1))
>>> d
array([[ 1,  2,  3,  4],
       [ 4,  5,  6,  7],
       [ 7,  8,  9, 10]])
>>> d
array([[ 1,  2,  3,  4],
       [ 4,  5,  6,  7],
       [ 7,  8,  9, 10]])
>>> c
array([[ 1,  2,  3],
       [ 4,  4,  5],
       [ 6,  7,  7],
       [ 8,  9, 10]])
>>> a[1] = -1
>>> a
array('i', [1, -1, 3, 4])
>>> d[1]=-1
>>> c
array([[ 1,  2,  3],
       [ 4, -1, -1],
       [-1, -1,  7],
       [ 8,  9, 10]])
>>> d
array([[ 1,  2,  3,  4],
       [-1, -1, -1, -1],
       [ 7,  8,  9, 10]])
>>> d[1]
array([-1, -1, -1, -1])
>>> d[0]
array([1, 2, 3, 4])
>>> d
array([[ 1,  2,  3,  4],
       [-1, -1, -1, -1],
       [ 7,  8,  9, 10]])
>>> numpy.sqrt(d)

Warning (from warnings module):
  File "__main__", line 1
RuntimeWarning: invalid value encountered in sqrt
array([[ 1.        ,  1.41421356,  1.73205081,  2.        ],
       [        nan,         nan,         nan,         nan],
       [ 2.64575131,  2.82842712,  3.        ,  3.16227766]])
>>> d[1] = [4,5,6,7]
>>> d
array([[ 1,  2,  3,  4],
       [ 4,  5,  6,  7],
       [ 7,  8,  9, 10]])
>>> numpy.sqrt(d)
array([[ 1.        ,  1.41421356,  1.73205081,  2.        ],
       [ 2.        ,  2.23606798,  2.44948974,  2.64575131],
       [ 2.64575131,  2.82842712,  3.        ,  3.16227766]])
>>> d
array([[ 1,  2,  3,  4],
       [ 4,  5,  6,  7],
       [ 7,  8,  9, 10]])
>>> d[1]
array([4, 5, 6, 7])
>>> d[:,1]
array([2, 5, 8])
>>> d[,1]
SyntaxError: invalid syntax
>>> d[:,0]
array([1, 4, 7])
>>> a[1:3,1:3]
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    a[1:3,1:3]
TypeError: array indices must be integers
>>> d[1:3,1:3]
array([[5, 6],
       [8, 9]])
>>> d[:]
array([[ 1,  2,  3,  4],
       [ 4,  5,  6,  7],
       [ 7,  8,  9, 10]])
>>> d[:,]
array([[ 1,  2,  3,  4],
       [ 4,  5,  6,  7],
       [ 7,  8,  9, 10]])
>>> d[:,1]
array([2, 5, 8])
>>> d[0:2,0:2]
array([[1, 2],
       [4, 5]])
>>> d += 1
>>> d
array([[ 2,  3,  4,  5],
       [ 5,  6,  7,  8],
       [ 8,  9, 10, 11]])
>>> d + [1,1,1,1]
array([[ 3,  4,  5,  6],
       [ 6,  7,  8,  9],
       [ 9, 10, 11, 12]])
>>> d
array([[ 2,  3,  4,  5],
       [ 5,  6,  7,  8],
       [ 8,  9, 10, 11]])
>>> numpy.where(d < 10,a,10)
array([[ 1, -1,  3,  4],
       [ 1, -1,  3,  4],
       [ 1, -1, 10, 10]], dtype=int32)
>>> d
array([[ 2,  3,  4,  5],
       [ 5,  6,  7,  8],
       [ 8,  9, 10, 11]])
>>> numpy.where(d < 10,a)
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    numpy.where(d < 10,a)
ValueError: either both or neither of x and y should be given
>>> numpy.where(d < 10,a,1)
array([[ 1, -1,  3,  4],
       [ 1, -1,  3,  4],
       [ 1, -1,  1,  1]], dtype=int32)
>>> numpy.where(d < 10,d,10)
array([[ 2,  3,  4,  5],
       [ 5,  6,  7,  8],
       [ 8,  9, 10, 10]])
>>> numpy.where(d < 10,d,1)
array([[2, 3, 4, 5],
       [5, 6, 7, 8],
       [8, 9, 1, 1]])
>>> a
array('i', [1, -1, 3, 4])
>>> a = array.array([-1,-2,-3,-4])
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    a = array.array([-1,-2,-3,-4])
TypeError: must be a unicode character, not list
>>> a = array.array('i',[-1,-2,-3,-4])
>>> a
array('i', [-1, -2, -3, -4])
>>> numpy.where(d < 10,a,1)
array([[-1, -2, -3, -4],
       [-1, -2, -3, -4],
       [-1, -2,  1,  1]], dtype=int32)
>>> a = array.array('i',[-1,-2,-3,-4,-5])
>>> numpy.where(d < 10,a,1)
Traceback (most recent call last):
  File "<pyshell#167>", line 1, in <module>
    numpy.where(d < 10,a,1)
ValueError: shape mismatch: objects cannot be broadcast to a single shape
>>> a = array.array('i',[-1,-2,-3,-4])
>>> numpy.where(d > 10,a,10)
array([[10, 10, 10, 10],
       [10, 10, 10, 10],
       [10, 10, 10, -4]], dtype=int32)
>>> d
array([[ 2,  3,  4,  5],
       [ 5,  6,  7,  8],
       [ 8,  9, 10, 11]])
>>> import numpy as ny
>>> import numpy as np
>>> del ny
>>> ny
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    ny
NameError: name 'ny' is not defined
>>> np
<module 'numpy' from 'E:\\Python34\\lib\\site-packages\\numpy\\__init__.py'>
>>> np.arange(0,1,0.1)
array([ 0. ,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9])
>>> np.linspace(0,1,12)
array([ 0.        ,  0.09090909,  0.18181818,  0.27272727,  0.36363636,
        0.45454545,  0.54545455,  0.63636364,  0.72727273,  0.81818182,
        0.90909091,  1.        ])
>>> np.linspace(0,1,num=12,endpoint=False)
array([ 0.        ,  0.08333333,  0.16666667,  0.25      ,  0.33333333,
        0.41666667,  0.5       ,  0.58333333,  0.66666667,  0.75      ,
        0.83333333,  0.91666667])
>>> np.linspace(0,1,num=12,endpoint=True)
array([ 0.        ,  0.09090909,  0.18181818,  0.27272727,  0.36363636,
        0.45454545,  0.54545455,  0.63636364,  0.72727273,  0.81818182,
        0.90909091,  1.        ])
>>> 1/12
0.08333333333333333
>>> 1/11
0.09090909090909091
>>> np.linspace(0,20,10)
array([  0.        ,   2.22222222,   4.44444444,   6.66666667,
         8.88888889,  11.11111111,  13.33333333,  15.55555556,
        17.77777778,  20.        ])
>>> np.linspace(0,20,11)
array([  0.,   2.,   4.,   6.,   8.,  10.,  12.,  14.,  16.,  18.,  20.])
>>> ipython
Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    ipython
NameError: name 'ipython' is not defined
>>> np.fromstring('abcdefghijklmn',dypte=np.int8)
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    np.fromstring('abcdefghijklmn',dypte=np.int8)
TypeError: 'dypte' is an invalid keyword argument for this function
>>> np.fromstring('abcdefghijklmn',dtype=np.int8)
array([ 97,  98,  99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110], dtype=int8)
>>> np.fromstring('abcdefghijklmn',dtype=np.int8,count=1)
array([97], dtype=int8)
>>> np.fromstring('abcdefghijklmn',dtype=np.int8,count=10)
array([ 97,  98,  99, 100, 101, 102, 103, 104, 105, 106], dtype=int8)
>>> np.fromstring('abcdefghijklmn',dtype=np.int8,count=-1)
array([ 97,  98,  99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110], dtype=int8)
>>> np.fromstring('abcdefghijklmn',dtype=np.int16)
array([25185, 25699, 26213, 26727, 27241, 27755, 28269], dtype=int16)
>>> hex(25185)
'0x6261'
>>> ord('a')
97
>>> hex(ord('a'))
'0x61'
>>> np.fromstring('abcdefghijklmn',dtype=np.float)
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    np.fromstring('abcdefghijklmn',dtype=np.float)
ValueError: string size must be a multiple of element size
>>> np.fromstring('abcdefghijklmn',dtype=float)
Traceback (most recent call last):
  File "<pyshell#195>", line 1, in <module>
    np.fromstring('abcdefghijklmn',dtype=float)
ValueError: string size must be a multiple of element size
>>> np.fromstring('abcdefghijklmn',dtype=np.int8)
array([ 97,  98,  99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110], dtype=int8)
>>> def myhash(i):
	return i%11

>>> np.fromfunction(myhash,(10,))
array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.])
>>> np.fromfunction(myhash,(10,2))
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    np.fromfunction(myhash,(10,2))
  File "E:\Python34\lib\site-packages\numpy\core\numeric.py", line 1808, in fromfunction
    return function(*args,**kwargs)
TypeError: myhash() takes 1 positional argument but 2 were given
>>> np.fromfunction(myhash,(10,1))
Traceback (most recent call last):
  File "<pyshell#202>", line 1, in <module>
    np.fromfunction(myhash,(10,1))
  File "E:\Python34\lib\site-packages\numpy\core\numeric.py", line 1808, in fromfunction
    return function(*args,**kwargs)
TypeError: myhash() takes 1 positional argument but 2 were given
>>> np.fromfunction(myhash,(10,))
array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.])
>>> def func2(i,j):
	return (i+1)*(j+1)

>>> np.fromfunction(func2,(4,4))
array([[  1.,   2.,   3.,   4.],
       [  2.,   4.,   6.,   8.],
       [  3.,   6.,   9.,  12.],
       [  4.,   8.,  12.,  16.]])
>>> def foo(i):
	return i

>>> np.fromfunction(foo,(4,))
array([ 0.,  1.,  2.,  3.])
>>> 
KeyboardInterrupt
>>> 
>>> 
>>> x = np.arange(10,1,-1)
>>> x
array([10,  9,  8,  7,  6,  5,  4,  3,  2])
>>> x[[3,3,1,8]]
array([7, 7, 9, 2])
>>> x
array([10,  9,  8,  7,  6,  5,  4,  3,  2])
>>> y = x[[3,3,1,8]]
>>> y
array([7, 7, 9, 2])
>>> y[0] = 5
>>> x
array([10,  9,  8,  7,  6,  5,  4,  3,  2])
>>> y
array([5, 7, 9, 2])
>>> y = x[xp.array([3,3,-3,4])]
Traceback (most recent call last):
  File "<pyshell#222>", line 1, in <module>
    y = x[xp.array([3,3,-3,4])]
NameError: name 'xp' is not defined
>>> np.array([3,3,-3,4])
array([ 3,  3, -3,  4])
>>> y = x[np.array([3,3,-3,4])]
>>> y
array([7, 7, 4, 6])
>>> x
>>> x
array([10,  9,  8,  7,  6,  5,  4,  3,  2])
>>> x
array([10,  9,  8,  7,  6,  5,  4,  3,  2])
>>> x = np.arange(0, 60, 10)
>>> x
array([ 0, 10, 20, 30, 40, 50])
>>> x.reshape(-1,-1)
Traceback (most recent call last):
  File "<pyshell#232>", line 1, in <module>
    x.reshape(-1,-1)
ValueError: can only specify one unknown dimension
>>> x.reshape(-1,1)
array([[ 0],
       [10],
       [20],
       [30],
       [40],
       [50]])
>>> x.reshape(1,-1)
array([[ 0, 10, 20, 30, 40, 50]])
>>> x
array([ 0, 10, 20, 30, 40, 50])
>>> x.reshape(-1,1) + np.arange(0,6)
array([[ 0,  1,  2,  3,  4,  5],
       [10, 11, 12, 13, 14, 15],
       [20, 21, 22, 23, 24, 25],
       [30, 31, 32, 33, 34, 35],
       [40, 41, 42, 43, 44, 45],
       [50, 51, 52, 53, 54, 55]])
>>> x.reshape(-1,1) + 1
array([[ 1],
       [11],
       [21],
       [31],
       [41],
       [51]])
>>> np.arange(0, 60, 10).reshape(-1,1) + 1
array([[ 1],
       [11],
       [21],
       [31],
       [41],
       [51]])
>>> np.arange(0, 60, 10).reshape(-1,1) + np.arange(0, 60, 10)
array([[  0,  10,  20,  30,  40,  50],
       [ 10,  20,  30,  40,  50,  60],
       [ 20,  30,  40,  50,  60,  70],
       [ 30,  40,  50,  60,  70,  80],
       [ 40,  50,  60,  70,  80,  90],
       [ 50,  60,  70,  80,  90, 100]])
>>> np.arange(0, 60, 10).reshape(-1,1) + np.arange(0, 6, 1)
array([[ 0,  1,  2,  3,  4,  5],
       [10, 11, 12, 13, 14, 15],
       [20, 21, 22, 23, 24, 25],
       [30, 31, 32, 33, 34, 35],
       [40, 41, 42, 43, 44, 45],
       [50, 51, 52, 53, 54, 55]])
>>> np.arange(0, 60, 10) + np.arange(0, 6, 1).reshape(-1,1)
array([[ 0, 10, 20, 30, 40, 50],
       [ 1, 11, 21, 31, 41, 51],
       [ 2, 12, 22, 32, 42, 52],
       [ 3, 13, 23, 33, 43, 53],
       [ 4, 14, 24, 34, 44, 54],
       [ 5, 15, 25, 35, 45, 55]])
>>> np.arange(0, 60, 10) + np.arange(0, 6, 1).reshape(-1,1)
array([[ 0, 10, 20, 30, 40, 50],
       [ 1, 11, 21, 31, 41, 51],
       [ 2, 12, 22, 32, 42, 52],
       [ 3, 13, 23, 33, 43, 53],
       [ 4, 14, 24, 34, 44, 54],
       [ 5, 15, 25, 35, 45, 55]])
>>> 
KeyboardInterrupt
>>> x=np.arange(0, 60, 10) + np.arange(0, 6, 1).reshape(-1,1)
>>> x
array([[ 0, 10, 20, 30, 40, 50],
       [ 1, 11, 21, 31, 41, 51],
       [ 2, 12, 22, 32, 42, 52],
       [ 3, 13, 23, 33, 43, 53],
       [ 4, 14, 24, 34, 44, 54],
       [ 5, 15, 25, 35, 45, 55]])
>>> x + np.arange(0,7)
Traceback (most recent call last):
  File "<pyshell#244>", line 1, in <module>
    x + np.arange(0,7)
ValueError: operands could not be broadcast together with shapes (6,6) (7,) 
>>> x + np.arange(0,5)
Traceback (most recent call last):
  File "<pyshell#245>", line 1, in <module>
    x + np.arange(0,5)
ValueError: operands could not be broadcast together with shapes (6,6) (5,) 
>>> x
array([[ 0, 10, 20, 30, 40, 50],
       [ 1, 11, 21, 31, 41, 51],
       [ 2, 12, 22, 32, 42, 52],
       [ 3, 13, 23, 33, 43, 53],
       [ 4, 14, 24, 34, 44, 54],
       [ 5, 15, 25, 35, 45, 55]])
>>> a
array('i', [-1, -2, -3, -4])
>>> b
Fraction(15, 4)
>>> y=np.arange(0, 60, 10)
>>> y[[1,2,3,4]]
array([10, 20, 30, 40])
>>> y[(1,1,1,1)]
Traceback (most recent call last):
  File "<pyshell#251>", line 1, in <module>
    y[(1,1,1,1)]
IndexError: too many indices
>>> y[[1,1,1,1]]
array([10, 10, 10, 10])
>>> x[3,[0,1]]
array([ 3, 13])
>>> x[1:3,[0,1]]
array([[ 1, 11],
       [ 2, 12]])
>>> y = x[3,[0,1]]
>>> y
array([ 3, 13])
>>> y[0]
3
>>> y[0] = -3
>>> x
array([[ 0, 10, 20, 30, 40, 50],
       [ 1, 11, 21, 31, 41, 51],
       [ 2, 12, 22, 32, 42, 52],
       [ 3, 13, 23, 33, 43, 53],
       [ 4, 14, 24, 34, 44, 54],
       [ 5, 15, 25, 35, 45, 55]])
>>> y
array([-3, 13])
>>> y = x[1:3,0:2]
>>> y
array([[ 1, 11],
       [ 2, 12]])
>>> y[0] = -1
>>> x
array([[ 0, 10, 20, 30, 40, 50],
       [-1, -1, 21, 31, 41, 51],
       [ 2, 12, 22, 32, 42, 52],
       [ 3, 13, 23, 33, 43, 53],
       [ 4, 14, 24, 34, 44, 54],
       [ 5, 15, 25, 35, 45, 55]])
>>> y[0] = [1,11]4
SyntaxError: invalid syntax
>>> y[0] = [1,11]
>>> x
array([[ 0, 10, 20, 30, 40, 50],
       [ 1, 11, 21, 31, 41, 51],
       [ 2, 12, 22, 32, 42, 52],
       [ 3, 13, 23, 33, 43, 53],
       [ 4, 14, 24, 34, 44, 54],
       [ 5, 15, 25, 35, 45, 55]])
>>> y
array([[ 1, 11],
       [ 2, 12]])
>>> y = x[[1,2],[3,4]]
>>> y
array([31, 42])
>>> y = x[(0,1),(0,1)]
>>> y
array([ 0, 11])
>>> persontype = np.dtype({
	'names':['name','age','weight'],
	'formats':['S32','i','f']})
>>> a = np.array([('Zhang',32,75.0),('huang',24,75.0)],dtype=persontype)
>>> a
array([(b'Zhang', 32, 75.0), (b'huang', 24, 75.0)], 
      dtype=[('name', 'S32'), ('age', '<i4'), ('weight', '<f4')])
>>> print(a)
[(b'Zhang', 32, 75.0) (b'huang', 24, 75.0)]
>>> 
KeyboardInterrupt
>>> a.dtype
dtype([('name', 'S32'), ('age', '<i4'), ('weight', '<f4')])
>>> persontype
dtype([('name', 'S32'), ('age', '<i4'), ('weight', '<f4')])
>>> a = np.array([('Zhang',0x12345678,75.0),('huang',24,75.0)],dtype=persontype)
>>> 
>>> a
array([(b'Zhang', 305419896, 75.0), (b'huang', 24, 75.0)], 
      dtype=[('name', 'S32'), ('age', '<i4'), ('weight', '<f4')])
>>> a.age
Traceback (most recent call last):
  File "<pyshell#284>", line 1, in <module>
    a.age
AttributeError: 'numpy.ndarray' object has no attribute 'age'
>>> a['age']
array([305419896,        24], dtype=int32)
>>> a['age'][0]
305419896
>>> hex(305419896)
'0x12345678'
>>> a[0]
(b'Zhang', 305419896, 75.0)
>>> a.tostring()
b'Zhang\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00xV4\x12\x00\x00\x96Bhuang\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x00\x00\x96B'
>>> hex(a.tostring())
Traceback (most recent call last):
  File "<pyshell#290>", line 1, in <module>
    hex(a.tostring())
TypeError: 'bytes' object cannot be interpreted as an integer
>>> for i in a.tostring():
	print(hex(i),end=' ')

	
0x5a 0x68 0x61 0x6e 0x67 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x78 0x56 0x34 0x12 0x0 0x0 0x96 0x42 0x68 0x75 0x61 0x6e 0x67 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x18 0x0 0x0 0x0 0x0 0x0 0x96 0x42 
>>> persontype = np.dtype({
	'names':['name','age','weight'],
	'formats':['S32','i','f']})
>>> persontype
dtype([('name', 'S32'), ('age', '<i4'), ('weight', '<f4')])
>>> persontype1 = persontype(
	[('name', 'S32'), ('age', '<i4'), ('weight', '<f4')])
Traceback (most recent call last):
  File "<pyshell#297>", line 2, in <module>
    [('name', 'S32'), ('age', '<i4'), ('weight', '<f4')])
TypeError: 'numpy.dtype' object is not callable
>>> persontype1 = np.dtype(
	[('name', 'S32'), ('age', '<i4'), ('weight', '<f4')])
>>> 
>>> persontype1
dtype([('name', 'S32'), ('age', '<i4'), ('weight', '<f4')])
>>> persontype1 == persontype
True
>>> def Q(L):
	H = [0]*11
	H[0] = 1
	for x in L:
		H[x+1] += 1
	return H

>>> Q([7,1,1,1])
[1, 0, 3, 0, 0, 0, 0, 0, 1, 0, 0]
>>> X = array([
        Q([7,1,1,1]),
        Q([8,8,0,9]), 
        Q([2,1,7,2]),
        Q([6,6,6,6]), 
        Q([1,1,1,1]), 
        Q([2,2,2,2]),
        Q([7,6,6,2]),
        Q([9,3,1,3]),
        Q([0,0,0,0]),
        Q([5,5,5,5]),
        Q([8,1,9,3]),
        Q([8,0,9,6]),
        Q([4,3,9,8]),
        Q([9,4,7,5]),
        Q([9,0,3,8]),
        Q([3,1,4,8])
    ])
Traceback (most recent call last):
  File "<pyshell#310>", line 17, in <module>
    Q([3,1,4,8])
TypeError: 'module' object is not callable
>>> X = np.array([
        Q([7,1,1,1]),
        Q([8,8,0,9]), 
        Q([2,1,7,2]),
        Q([6,6,6,6]), 
        Q([1,1,1,1]), 
        Q([2,2,2,2]),
        Q([7,6,6,2]),
        Q([9,3,1,3]),
        Q([0,0,0,0]),
        Q([5,5,5,5]),
        Q([8,1,9,3]),
        Q([8,0,9,6]),
        Q([4,3,9,8]),
        Q([9,4,7,5]),
        Q([9,0,3,8]),
        Q([3,1,4,8])
    ])
>>> 
>>> x
array([[ 0, 10, 20, 30, 40, 50],
       [ 1, 11, 21, 31, 41, 51],
       [ 2, 12, 22, 32, 42, 52],
       [ 3, 13, 23, 33, 43, 53],
       [ 4, 14, 24, 34, 44, 54],
       [ 5, 15, 25, 35, 45, 55]])
>>> X
array([[1, 0, 3, 0, 0, 0, 0, 0, 1, 0, 0],
       [1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 1],
       [1, 0, 1, 2, 0, 0, 0, 0, 1, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
       [1, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0],
       [1, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0],
       [1, 0, 0, 1, 0, 0, 0, 2, 1, 0, 0],
       [1, 0, 1, 0, 2, 0, 0, 0, 0, 0, 1],
       [1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [1, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0],
       [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1],
       [1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
       [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1],
       [1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
       [1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
       [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0]])
>>> Y = np.array([0,6,0,4,0,0,2,1,4,0,3,5,3,1,4,2])[:,None]
>>> Y
array([[0],
       [6],
       [0],
       [4],
       [0],
       [0],
       [2],
       [1],
       [4],
       [0],
       [3],
       [5],
       [3],
       [1],
       [4],
       [2]])
>>> Y = np.array([0,6,0,4,0,0,2,1,4,0,3,5,3,1,4,2]).reshape(-1:1)
SyntaxError: invalid syntax
>>> Y = np.array([0,6,0,4,0,0,2,1,4,0,3,5,3,1,4,2]).reshape(-1,1)
>>> Y
array([[0],
       [6],
       [0],
       [4],
       [0],
       [0],
       [2],
       [1],
       [4],
       [0],
       [3],
       [5],
       [3],
       [1],
       [4],
       [2]])
>>> Y = np.array([0,6,0,4,0,0,2,1,4,0,3,5,3,1,4,2])[:,-1]
Traceback (most recent call last):
  File "<pyshell#320>", line 1, in <module>
    Y = np.array([0,6,0,4,0,0,2,1,4,0,3,5,3,1,4,2])[:,-1]
SystemError: error return without exception set
>>> Y = np.array([0,6,0,4,0,0,2,1,4,0,3,5,3,1,4,2])[:,0]
Traceback (most recent call last):
  File "<pyshell#321>", line 1, in <module>
    Y = np.array([0,6,0,4,0,0,2,1,4,0,3,5,3,1,4,2])[:,0]
IndexError: too many indices
>>> Y = np.array([0,6,0,4,0,0,2,1,4,0,3,5,3,1,4,2])[:,NOne]
Traceback (most recent call last):
  File "<pyshell#322>", line 1, in <module>
    Y = np.array([0,6,0,4,0,0,2,1,4,0,3,5,3,1,4,2])[:,NOne]
NameError: name 'NOne' is not defined
>>> Y = np.array([0,6,0,4,0,0,2,1,4,0,3,5,3,1,4,2])[:,None]
>>> a
array([(b'Zhang', 305419896, 75.0), (b'huang', 24, 75.0)], 
      dtype=[('name', 'S32'), ('age', '<i4'), ('weight', '<f4')])
>>> b
Fraction(15, 4)
>>> aa = np.arange(0, 60, 10)
>>> a
array([(b'Zhang', 305419896, 75.0), (b'huang', 24, 75.0)], 
      dtype=[('name', 'S32'), ('age', '<i4'), ('weight', '<f4')])
>>> aa
array([ 0, 10, 20, 30, 40, 50])
>>> aa[:]
array([ 0, 10, 20, 30, 40, 50])
>>> aa[:,1]
Traceback (most recent call last):
  File "<pyshell#330>", line 1, in <module>
    aa[:,1]
IndexError: too many indices
>>> aa[:,None]
array([[ 0],
       [10],
       [20],
       [30],
       [40],
       [50]])
>>> aa[:,None][None,:]
array([[[ 0],
        [10],
        [20],
        [30],
        [40],
        [50]]])
>>> aa
array([ 0, 10, 20, 30, 40, 50])
>>> bb = aa[:,None]
>>> bb
array([[ 0],
       [10],
       [20],
       [30],
       [40],
       [50]])
>>> bb[None,:]
array([[[ 0],
        [10],
        [20],
        [30],
        [40],
        [50]]])
>>> bb[:]
array([[ 0],
       [10],
       [20],
       [30],
       [40],
       [50]])
>>> bb[0]
array([0])
>>> bb[1]
array([10])
>>> aa[0]
0
>>> aa[1]
10
>>> bb[0][0]
0
>>> bb[0][None]
array([[0]])
>>> bb[None]
array([[[ 0],
        [10],
        [20],
        [30],
        [40],
        [50]]])
>>> aa[None]
array([[ 0, 10, 20, 30, 40, 50]])
>>> alist = [10,20,30]
>>> alist[None]
Traceback (most recent call last):
  File "<pyshell#347>", line 1, in <module>
    alist[None]
TypeError: list indices must be integers, not NoneType
>>> aa
array([ 0, 10, 20, 30, 40, 50])
>>> aa[None][0]
array([ 0, 10, 20, 30, 40, 50])
>>> aa
array([ 0, 10, 20, 30, 40, 50])
>>> aa[0]
0
>>> aa[:None]
array([ 0, 10, 20, 30, 40, 50])
>>> aa[:,None]
array([[ 0],
       [10],
       [20],
       [30],
       [40],
       [50]])
>>> aa[1,None]
array([10])
>>> aa[1,1]
Traceback (most recent call last):
  File "<pyshell#355>", line 1, in <module>
    aa[1,1]
IndexError: too many indices
>>> aa[1,None]
array([10])
>>> aa[(1,2),None]
array([[10],
       [20]])
>>> Y
array([[0],
       [6],
       [0],
       [4],
       [0],
       [0],
       [2],
       [1],
       [4],
       [0],
       [3],
       [5],
       [3],
       [1],
       [4],
       [2]])
>>> a
array([(b'Zhang', 305419896, 75.0), (b'huang', 24, 75.0)], 
      dtype=[('name', 'S32'), ('age', '<i4'), ('weight', '<f4')])
>>> aa
array([ 0, 10, 20, 30, 40, 50])
>>> cc = aa.reshape(2,3)
>>> cc
array([[ 0, 10, 20],
       [30, 40, 50]])
>>> cc[:,None)
SyntaxError: invalid syntax
>>> cc[:,None]
array([[[ 0, 10, 20]],

       [[30, 40, 50]]])
>>> cc[1]
array([30, 40, 50])
>>> cc[2]
Traceback (most recent call last):
  File "<pyshell#366>", line 1, in <module>
    cc[2]
IndexError: index 2 is out of bounds for axis 0 with size 2
>>> cc[0]
array([ 0, 10, 20])
>>> X_ = linalg.pinv(X)
Traceback (most recent call last):
  File "<pyshell#368>", line 1, in <module>
    X_ = linalg.pinv(X)
NameError: name 'linalg' is not defined
>>> X_ = np.linalg.pinv(X)
>>> X_
array([[  2.44123290e-02,   1.13844231e-02,   3.40156013e-02,
          1.63355000e-02,  -8.11226911e-03,   1.10942754e-02,
          4.14378497e-02,   1.41986502e-02,   2.98248985e-02,
          2.49664450e-02,   8.04939074e-03,   5.62845426e-03,
          4.30711790e-02,   5.39803739e-02,   1.75336826e-02,
          5.67946010e-02],
       [ -4.59854576e-03,  -8.83974146e-03,  -8.54524344e-03,
         -6.97158593e-03,   5.78863356e-03,  -2.10476181e-03,
         -1.29520043e-02,  -1.17533449e-03,   2.32916486e-01,
         -6.52394839e-03,  -3.33985196e-02,   1.53288140e-02,
         -2.13944556e-02,  -1.23657449e-02,   2.33834436e-02,
         -4.70133794e-03],
       [  6.65690115e-02,  -1.20027248e-02,  -2.16170239e-02,
          1.80975584e-02,   1.93924577e-01,   1.75525062e-02,
         -6.54375155e-02,  -1.99109525e-03,  -3.69565833e-03,
         -5.12138198e-03,   1.77056194e-02,   2.00232591e-02,
         -1.25211469e-02,  -1.79760105e-02,  -3.16994394e-02,
         -7.96438100e-03],
       [ -4.96670211e-02,  -9.07532879e-03,   4.88729675e-02,
         -4.73970601e-03,   2.23541423e-02,   2.19434119e-01,
         -1.39439510e-02,  -4.88273503e-03,  -6.78741757e-03,
         -3.68450115e-03,  -3.33633692e-03,   8.38518752e-03,
          4.79293552e-03,  -2.37235339e-02,  -1.06217269e-02,
         -1.95309401e-02],
       [  9.08638893e-03,  -1.12259297e-01,   6.06985068e-02,
         -1.98634319e-02,  -1.70776065e-01,  -6.75518291e-02,
          1.10348764e-01,   2.97888033e-01,   3.37798115e-02,
          4.50334150e-02,   6.72448833e-02,  -1.79705340e-01,
         -1.14184714e-02,  -2.18595199e-01,   1.18383852e-01,
          1.91552132e-01],
       [ -1.09844877e-01,  -1.55259787e-01,  -1.21318834e-01,
          6.68241973e-02,   1.08039300e-01,   8.50913842e-02,
         -1.36189407e-01,  -1.71949545e-01,   7.93423859e-02,
         -9.18382794e-02,  -1.60017552e-01,  -3.33795144e-02,
          3.20445060e-01,   3.28891579e-01,  -1.67191780e-01,
          3.12201822e-01],
       [ -1.05096394e-02,   3.01719273e-03,  -1.21920170e-02,
         -5.73385968e-04,   3.14829654e-03,  -2.16458748e-04,
         -1.32116694e-02,  -1.85513512e-03,  -7.73856175e-03,
          2.41021669e-01,   1.94188609e-03,  -9.74465570e-03,
         -2.84927853e-02,  -2.54821264e-03,  -7.79828484e-04,
         -7.42054049e-03],
       [ -2.63739010e-02,  -2.26356934e-02,  -4.01933512e-02,
          2.02062280e-01,   2.42095007e-02,  -3.42939985e-03,
          5.56427634e-02,  -1.63378540e-03,  -1.03439355e-02,
         -2.73112221e-03,  -7.81555989e-03,   4.20038160e-02,
         -4.38934722e-03,  -2.75370496e-02,  -1.64539189e-02,
         -6.53514161e-03],
       [  2.63910306e-01,   6.00559264e-02,   2.86393075e-01,
         -1.51711450e-01,  -2.82973087e-01,  -2.38007549e-01,
          3.40782509e-01,   3.46554839e-03,  -1.27197775e-02,
         -2.72285275e-02,  -2.02092629e-03,  -1.13180756e-01,
         -1.22776304e-01,   7.04525715e-02,   6.55424011e-02,
          1.38621936e-02],
       [  5.65407987e-02,   3.15547677e-01,   7.18522835e-02,
         -5.07397893e-02,  -9.81384659e-02,  -6.75154962e-02,
          8.78958793e-02,  -1.90099392e-01,  -1.01262188e-01,
          5.40722404e-02,   6.31146078e-02,  -1.12941398e-02,
         -2.33134686e-02,  -2.54750500e-01,   6.23336772e-02,
          2.39602430e-01],
       [ -9.74632055e-02,  -1.30105310e-02,  -1.27887958e-01,
          1.29573140e-02,   1.61974091e-01,   1.01124587e-01,
         -1.87183970e-01,   1.29028042e-01,  -8.41915509e-02,
         -1.03133783e-01,   8.87794607e-02,   2.84077146e-01,
          7.13526988e-02,   3.74073595e-01,   2.72380502e-02,
         -4.83887832e-01]])
>>> aa
array([ 0, 10, 20, 30, 40, 50])
>>> bb
array([[ 0],
       [10],
       [20],
       [30],
       [40],
       [50]])
>>> cc
array([[ 0, 10, 20],
       [30, 40, 50]])
>>> cc[0,None]
array([[ 0, 10, 20]])
>>> cc[0,:]
array([ 0, 10, 20])
>>> aa[:,:]
Traceback (most recent call last):
  File "<pyshell#376>", line 1, in <module>
    aa[:,:]
IndexError: too many indices
>>> aa[:,None]
array([[ 0],
       [10],
       [20],
       [30],
       [40],
       [50]])
>>> cc[0,1]
10
>>> aa[:,None].reshape(1,-1)
array([[ 0, 10, 20, 30, 40, 50]])
>>> persontype
dtype([('name', 'S32'), ('age', '<i4'), ('weight', '<f4')])
>>> dir(persontype)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', 'alignment', 'base', 'byteorder', 'char', 'descr', 'fields', 'flags', 'hasobject', 'isalignedstruct', 'isbuiltin', 'isnative', 'itemsize', 'kind', 'metadata', 'name', 'names', 'newbyteorder', 'num', 'shape', 'str', 'subdtype', 'type']
>>> persontype.names
('name', 'age', 'weight')
>>> persontype.formats
Traceback (most recent call last):
  File "<pyshell#383>", line 1, in <module>
    persontype.formats
AttributeError: 'numpy.dtype' object has no attribute 'formats'
>>> persontype.names
('name', 'age', 'weight')
>>> persontype.name
'void320'
>>> persontype.age
Traceback (most recent call last):
  File "<pyshell#386>", line 1, in <module>
    persontype.age
AttributeError: 'numpy.dtype' object has no attribute 'age'
>>> persontype.type
<class 'numpy.void'>
>>> persontype.subtype
Traceback (most recent call last):
  File "<pyshell#388>", line 1, in <module>
    persontype.subtype
AttributeError: 'numpy.dtype' object has no attribute 'subtype'
>>> persontype.num
20
>>> len(persontype)
3
>>> a
array([(b'Zhang', 305419896, 75.0), (b'huang', 24, 75.0)], 
      dtype=[('name', 'S32'), ('age', '<i4'), ('weight', '<f4')])
>>> len(a)
2
>>> a
array([(b'Zhang', 305419896, 75.0), (b'huang', 24, 75.0)], 
      dtype=[('name', 'S32'), ('age', '<i4'), ('weight', '<f4')])
>>> a[0]
(b'Zhang', 305419896, 75.0)
>>> len(a[0])
3
>>> a = np.array([('Zhang',23,1.5),('z',10,1.0)],dtype= persontype)
>>> a
array([(b'Zhang', 23, 1.5), (b'z', 10, 1.0)], 
      dtype=[('name', 'S32'), ('age', '<i4'), ('weight', '<f4')])
>>> persontype
dtype([('name', 'S32'), ('age', '<i4'), ('weight', '<f4')])
>>> persontype1
dtype([('name', 'S32'), ('age', '<i4'), ('weight', '<f4')])
>>> dir(persontype1)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', 'alignment', 'base', 'byteorder', 'char', 'descr', 'fields', 'flags', 'hasobject', 'isalignedstruct', 'isbuiltin', 'isnative', 'itemsize', 'kind', 'metadata', 'name', 'names', 'newbyteorder', 'num', 'shape', 'str', 'subdtype', 'type']
>>> persontype1.names
('name', 'age', 'weight')
>>> a[0]
(b'Zhang', 23, 1.5)
>>> a
array([(b'Zhang', 23, 1.5), (b'z', 10, 1.0)], 
      dtype=[('name', 'S32'), ('age', '<i4'), ('weight', '<f4')])
>>> ftype = np.dtype([('f1', [('f2', np.int16)])])
>>> ftype
dtype([('f1', [('f2', '<i2')])])
>>> a = np.array([10,20],dtype=ftype)
Traceback (most recent call last):
  File "<pyshell#407>", line 1, in <module>
    a = np.array([10,20],dtype=ftype)
TypeError: expected an object with a buffer interface
>>> a = np.array([10,20])
>>> a = np.array([(10),(20)],dtype=ftype)
Traceback (most recent call last):
  File "<pyshell#409>", line 1, in <module>
    a = np.array([(10),(20)],dtype=ftype)
TypeError: expected an object with a buffer interface
>>> a = np.array([(10,),(20,)],dtype=ftype)
Traceback (most recent call last):
  File "<pyshell#410>", line 1, in <module>
    a = np.array([(10,),(20,)],dtype=ftype)
TypeError: expected an object with a buffer interface
>>> a = np.array([10,20],dtype=ftype)
Traceback (most recent call last):
  File "<pyshell#411>", line 1, in <module>
    a = np.array([10,20],dtype=ftype)
TypeError: expected an object with a buffer interface
>>> a = np.array([10,20],dtype=np.int16)
>>> a
array([10, 20], dtype=int16)
>>> ftype
dtype([('f1', [('f2', '<i2')])])
>>> np.int16
<class 'numpy.int16'>
>>> ftype['f1']
dtype([('f2', '<i2')])
>>> dt = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))])
>>> x = np.array([('Sarah', (8.0, 7.0)), ('John', (6.0, 7.0))], dtype=dt)
>>> dt = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,2))])
>>> x = np.array([('Sarah', ((8.0, 7.0),(8.0, 7.0))), ('John', ((6.0, 7.0),(8.0, 7.0)))], dtype=dt)
>>> x
array([('Sarah', [[8.0, 7.0], [8.0, 7.0]]),
       ('John', [[6.0, 7.0], [8.0, 7.0]])], 
      dtype=[('name', '<U16'), ('grades', '<f8', (2, 2))])
>>> x[0]
('Sarah', [[8.0, 7.0], [8.0, 7.0]])
>>> x[0][1]
array([[ 8.,  7.],
       [ 8.,  7.]])
>>> x[0][1][0]
array([ 8.,  7.])
>>> a = np.array([(10,),(20,)],dtype=ftype)
Traceback (most recent call last):
  File "<pyshell#425>", line 1, in <module>
    a = np.array([(10,),(20,)],dtype=ftype)
TypeError: expected an object with a buffer interface
>>> persontype
dtype([('name', 'S32'), ('age', '<i4'), ('weight', '<f4')])
>>> a
array([10, 20], dtype=int16)
>>> a = np.array([('Zhang',23,1.5),('z',10,1.0)],dtype= persontype)
>>> a
array([(b'Zhang', 23, 1.5), (b'z', 10, 1.0)], 
      dtype=[('name', 'S32'), ('age', '<i4'), ('weight', '<f4')])
>>> a = np.array([('Zhang',0x01010101,1.5),('z',10,1.0)],dtype= persontype)
>>> a
array([(b'Zhang', 16843009, 1.5), (b'z', 10, 1.0)], 
      dtype=[('name', 'S32'), ('age', '<i4'), ('weight', '<f4')])
>>> a = np.array([('Zhang',0x01020304,1.5),('z',10,1.0)],dtype= persontype)
>>> x = 0x01020304
>>> x
16909060
>>> hex(x)
'0x1020304'
>>> 
KeyboardInterrupt
>>> a
array([(b'Zhang', 16909060, 1.5), (b'z', 10, 1.0)], 
      dtype=[('name', 'S32'), ('age', '<i4'), ('weight', '<f4')])
>>> x[0]
Traceback (most recent call last):
  File "<pyshell#437>", line 1, in <module>
    x[0]
TypeError: 'int' object is not subscriptable
>>> bit(x)
Traceback (most recent call last):
  File "<pyshell#438>", line 1, in <module>
    bit(x)
NameError: name 'bit' is not defined
>>> bin(x)
'0b1000000100000001100000100'
>>> persontype
dtype([('name', 'S32'), ('age', '<i4'), ('weight', '<f4')])
>>> len(bin(x))
27
>>> x = bin(x)
>>> x
'0b1000000100000001100000100'
>>> hex(x)
Traceback (most recent call last):
  File "<pyshell#444>", line 1, in <module>
    hex(x)
TypeError: 'str' object cannot be interpreted as an integer
>>> x
'0b1000000100000001100000100'
>>> x = 0x01020304
>>> x
16909060
>>> hex(x)
'0x1020304'
>>> x.tobyte(4,'little')
Traceback (most recent call last):
  File "<pyshell#449>", line 1, in <module>
    x.tobyte(4,'little')
AttributeError: 'int' object has no attribute 'tobyte'
>>> x.to_bytes(4,'little')
b'\x04\x03\x02\x01'
>>> data = 10
>>> b.to_byte(4,'little')
Traceback (most recent call last):
  File "<pyshell#452>", line 1, in <module>
    b.to_byte(4,'little')
AttributeError: 'Fraction' object has no attribute 'to_byte'
>>> data.to_bytes(4,'little')
b'\n\x00\x00\x00'
>>> data.to_bytes(8,'little')
b'\n\x00\x00\x00\x00\x00\x00\x00'
>>> hi, lo = struct.unpack('>QQ', b'\n\x00\x00\x00\x00\x00\x00\x00')
Traceback (most recent call last):
  File "<pyshell#455>", line 1, in <module>
    hi, lo = struct.unpack('>QQ', b'\n\x00\x00\x00\x00\x00\x00\x00')
NameError: name 'struct' is not defined
>>> import struct
>>> hi, lo = struct.unpack('>QQ', b'\n\x00\x00\x00\x00\x00\x00\x00')
Traceback (most recent call last):
  File "<pyshell#457>", line 1, in <module>
    hi, lo = struct.unpack('>QQ', b'\n\x00\x00\x00\x00\x00\x00\x00')
struct.error: unpack requires a bytes object of length 16
>>> hi, lo = struct.unpack('>ii', b'\n\x00\x00\x00\x00\x00\x00\x00')
>>> hi
167772160
>>> ho
Traceback (most recent call last):
  File "<pyshell#460>", line 1, in <module>
    ho
NameError: name 'ho' is not defined
>>> hi= struct.unpack('>i', b'\n\x00\x00\x00\x00\x00\x00\x00')
Traceback (most recent call last):
  File "<pyshell#461>", line 1, in <module>
    hi= struct.unpack('>i', b'\n\x00\x00\x00\x00\x00\x00\x00')
struct.error: unpack requires a bytes object of length 4
>>> hi,ho= struct.unpack('>ii', b'\n\x00\x00\x00\x00\x00\x00\x00')
>>> ho
0
>>> hi
167772160
>>> hi,ho = struct.unpack('ii', b'\n\x00\x00\x00\x00\x00\x00\x00')
>>> hi
10
>>> ho
0
>>> struct.pack('ii',10,0)
b'\n\x00\x00\x00\x00\x00\x00\x00'
>>> dt = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,2))])
>>> dr
Traceback (most recent call last):
  File "<pyshell#470>", line 1, in <module>
    dr
NameError: name 'dr' is not defined
>>> dt
dtype([('name', '<U16'), ('grades', '<f8', (2, 2))])
>>> np.str0
<class 'numpy.str_'>
>>> np.str_
<class 'numpy.str_'>
>>> S32
Traceback (most recent call last):
  File "<pyshell#474>", line 1, in <module>
    S32
NameError: name 'S32' is not defined
>>> np.float64
<class 'numpy.float64'>
>>> dt = np.dtype(np.int32)
>>> dt
dtype('int32')
>>> dt = np.dtype([('name', np.int32), ('grades', np.float64, (2,2))])
>>> dt
dtype([('name', '<i4'), ('grades', '<f8', (2, 2))])
>>> dt = np.dtype([('name', '<i4'), ('grades', np.float64, (2,2))])
>>> dt
dtype([('name', '<i4'), ('grades', '<f8', (2, 2))])
>>> dt = np.dtype([('name', '<i4'), ('grades', 'f8', (2,2))])
>>> dt
dtype([('name', '<i4'), ('grades', '<f8', (2, 2))])
>>> dt = np.dtype([('name', '<U0'), ('grades', np.float64, (2,2))])
>>> dt
dtype([('name', '<U'), ('grades', '<f8', (2, 2))])
>>> dt = np.dtype([('name', '<U10'), ('grades', np.float64, (2,2))])
>>> x = np.array([('Sarahdfefe', ((8.0, 7.0),(8.0, 7.0))), ('John', ((6.0, 7.0),(8.0, 7.0)))], dtype=dt)
>>> x = np.array([('Sarahdfefed', ((8.0, 7.0),(8.0, 7.0))), ('John', ((6.0, 7.0),(8.0, 7.0)))], dtype=dt)
>>> x
array([('Sarahdfefe', [[8.0, 7.0], [8.0, 7.0]]),
       ('John', [[6.0, 7.0], [8.0, 7.0]])], 
      dtype=[('name', '<U10'), ('grades', '<f8', (2, 2))])
>>> x[0]
('Sarahdfefe', [[8.0, 7.0], [8.0, 7.0]])
>>> x[0][0]
'Sarahdfefe'
>>> x = np.array([('Sarahdfefed', ((8.0, 7.0),(8.0, 7.0))), ('John', ((6.0, 7.0),(8.0, 7.0)))], dtype=dt)
>>> x
array([('Sarahdfefe', [[8.0, 7.0], [8.0, 7.0]]),
       ('John', [[6.0, 7.0], [8.0, 7.0]])], 
      dtype=[('name', '<U10'), ('grades', '<f8', (2, 2))])
>>> x = np.array([('Sarahdfefeddddd', ((8.0, 7.0),(8.0, 7.0))), ('John', ((6.0, 7.0),(8.0, 7.0)))], dtype=dt)
>>> x
array([('Sarahdfefe', [[8.0, 7.0], [8.0, 7.0]]),
       ('John', [[6.0, 7.0], [8.0, 7.0]])], 
      dtype=[('name', '<U10'), ('grades', '<f8', (2, 2))])
>>> dt = np.dtype('i4')
>>> dt
dtype('int32')
>>> dt = np.dtype([('name', np.complex128), ('grades', np.float64, (2,2))])
\
>>> dt
dtype([('name', '<c16'), ('grades', '<f8', (2, 2))])
\
>>> dt
dtype([('name', '<c16'), ('grades', '<f8', (2, 2))])
>>> dt = np.dtype([('name', 'c16'), ('grades', np.float64, (2,2))])
>>> dt
dtype([('name', '<c16'), ('grades', '<f8', (2, 2))])
>>> dt = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,2))])
>>> dt
dtype([('name', '<U16'), ('grades', '<f8', (2, 2))])
>>> dt = np.dtype([('name', np.str, 16), ('grades', np.float64, (2,2))])
>>> dt
dtype([('name', '<U16'), ('grades', '<f8', (2, 2))])
>>> dt = np.dtype([('name', np.str16), ('grades', np.float64, (2,2))])
Traceback (most recent call last):
  File "<pyshell#507>", line 1, in <module>
    dt = np.dtype([('name', np.str16), ('grades', np.float64, (2,2))])
AttributeError: 'module' object has no attribute 'str16'
>>> dt = np.dtype([('name', np.str,16), ('grades', np.float64, (2,2))])
>>> dt
dtype([('name', '<U16'), ('grades', '<f8', (2, 2))])
>>> np.dtype("i4, (2,3)f8")
dtype([('f0', '<i4'), ('f1', '<f8', (2, 3))])
>>> x = np.dtype("i4, (2,3)f8")
>>> x.names
('f0', 'f1')
>>> np.dtype([('f2', np.int16)])
dtype([('f2', '<i2')])
>>> atype = np.dtype([('f2', np.int16)])
>>> a = np.array([20,30],dtype=atype)
Traceback (most recent call last):
  File "<pyshell#515>", line 1, in <module>
    a = np.array([20,30],dtype=atype)
TypeError: expected an object with a buffer interface
>>> a = np.array([(20),(30)],dtype=atype)
Traceback (most recent call last):
  File "<pyshell#516>", line 1, in <module>
    a = np.array([(20),(30)],dtype=atype)
TypeError: expected an object with a buffer interface
>>> atype = np.dtype([('f2', np.int16),('age', '<i4')])
>>> atype
dtype([('f2', '<i2'), ('age', '<i4')])
>>> (20)
20
>>> aatype = np.dtype([('f2', np.int16)])
>>> a = np.array([(20,),(30,)],dtype=atype)
Traceback (most recent call last):
  File "<pyshell#521>", line 1, in <module>
    a = np.array([(20,),(30,)],dtype=atype)
ValueError: size of tuple must match number of fields.
>>> atype.fields
mappingproxy({'f2': (dtype('int16'), 0), 'age': (dtype('int32'), 2)})
>>> a = np.array([(20,),(30,)],dtype=aatype)
>>> a
array([(20,), (30,)], 
      dtype=[('f2', '<i2')])
>>> bbtype = np.dtype([('f1', aatype)])
>>> b = np.array([(a,),(a,)],dtype=bbtype)
>>> b
array([((20,),), ((20,),)], 
      dtype=[('f1', [('f2', '<i2')])])
>>> bbtype
dtype([('f1', [('f2', '<i2')])])
>>> b = np.array([(20,),(20,)],dtype=bbtype)
Traceback (most recent call last):
  File "<pyshell#529>", line 1, in <module>
    b = np.array([(20,),(20,)],dtype=bbtype)
TypeError: expected an object with a buffer interface
>>> b = np.array([((a,),),((a,).)],dtype=bbtype)
SyntaxError: invalid syntax
>>> b = np.array([((a,),),((a,),)],dtype=bbtype)
Traceback (most recent call last):
  File "<pyshell#531>", line 1, in <module>
    b = np.array([((a,),),((a,),)],dtype=bbtype)
ValueError: setting an array element with a sequence.
>>> b = np.array([((20,),),((20,),)],dtype=bbtype)
>>> b
array([((20,),), ((20,),)], 
      dtype=[('f1', [('f2', '<i2')])])
>>> bbtype
dtype([('f1', [('f2', '<i2')])])
>>> bbtype.names
('f1',)
>>> bbtype.fields
mappingproxy({'f1': (dtype([('f2', '<i2')]), 0)})
>>> b = np.array([((20,30,),),((20,),)],dtype=bbtype)
Traceback (most recent call last):
  File "<pyshell#537>", line 1, in <module>
    b = np.array([((20,30,),),((20,),)],dtype=bbtype)
ValueError: size of tuple must match number of fields.
>>> bbtype = np.dtype([('f1', [('f2','i4'),('f3','i4')]),('f4','i4')])
>>> bbtype
dtype([('f1', [('f2', '<i4'), ('f3', '<i4')]), ('f4', '<i4')])
>>> bbtype['f1']
dtype([('f2', '<i4'), ('f3', '<i4')])
>>> b = np.array([((12,34),1234),((56,78),1234)],dtype=bbtype)
>>> b
array([((12, 34), 1234), ((56, 78), 1234)], 
      dtype=[('f1', [('f2', '<i4'), ('f3', '<i4')]), ('f4', '<i4')])
>>> b = np.array([([(12,34),(56,78)],1234),((56,78),1234)],dtype=bbtype)
Traceback (most recent call last):
  File "<pyshell#543>", line 1, in <module>
    b = np.array([([(12,34),(56,78)],1234),((56,78),1234)],dtype=bbtype)
TypeError: expected an object with a buffer interface
>>> b = np.array([((12,34),1234),((56,78),1234)],dtype=bbtype)
>>> b
array([((12, 34), 1234), ((56, 78), 1234)], 
      dtype=[('f1', [('f2', '<i4'), ('f3', '<i4')]), ('f4', '<i4')])
>>> b = np.array([(('a',34),1234),((56,78),1234)],dtype=bbtype)
Traceback (most recent call last):
  File "<pyshell#546>", line 1, in <module>
    b = np.array([(('a',34),1234),((56,78),1234)],dtype=bbtype)
ValueError: invalid literal for int() with base 10: 'a'
>>> 
>>> 
>>> bbtype = np.dtype(('f1', [('f2','i4'),('f3','i4')]),('f4','i4'))
Traceback (most recent call last):
  File "<pyshell#549>", line 1, in <module>
    bbtype = np.dtype(('f1', [('f2','i4'),('f3','i4')]),('f4','i4'))
ValueError: mismatch in size of old and new data-descriptor
>>> bbtype = np.dtype('f4','i4')
>>> bbtype
dtype('float32')
>>> bbtype = np.dtype([('f1', [('f2','i4'),('f3','i4')]),('f4','i4')])
>>> bbtype = np.dtype([('f1', [('f2','i4',2),('f3','i4')]),('f4','i4',2)])
>>> b = np.array([(((10,20),(30,40)),(50,60))],dtype=bbtype)
Traceback (most recent call last):
  File "<pyshell#554>", line 1, in <module>
    b = np.array([(((10,20),(30,40)),(50,60))],dtype=bbtype)
ValueError: setting an array element with a sequence.
>>> b = np.array([(((10,20),(30,40)),(50,60)),],dtype=bbtype)
Traceback (most recent call last):
  File "<pyshell#555>", line 1, in <module>
    b = np.array([(((10,20),(30,40)),(50,60)),],dtype=bbtype)
ValueError: setting an array element with a sequence.
>>> b = np.array([(((10,20),(30,40),),(50,60)),],dtype=bbtype)
Traceback (most recent call last):
  File "<pyshell#556>", line 1, in <module>
    b = np.array([(((10,20),(30,40),),(50,60)),],dtype=bbtype)
ValueError: setting an array element with a sequence.
>>> b = np.array([(((10,20),(30,40),),(50,60),),],dtype=bbtype)
Traceback (most recent call last):
  File "<pyshell#557>", line 1, in <module>
    b = np.array([(((10,20),(30,40),),(50,60),),],dtype=bbtype)
ValueError: setting an array element with a sequence.
>>> bbtype = np.dtype([('f1', [('f2','i4'),('f3','i4')]),('f4','i4',2)])
>>> b = np.array([(20,30),(50,60))],dtype=bbtype)
SyntaxError: invalid syntax
>>> b = np.array([(20,30),(50,60)],dtype=bbtype)
Traceback (most recent call last):
  File "<pyshell#560>", line 1, in <module>
    b = np.array([(20,30),(50,60)],dtype=bbtype)
TypeError: expected an object with a buffer interface
>>> b = np.array([(20,30),50,60)],dtype=bbtype)
SyntaxError: invalid syntax
>>> b = np.array([(20,30),50,60],dtype=bbtype)
Traceback (most recent call last):
  File "<pyshell#562>", line 1, in <module>
    b = np.array([(20,30),50,60],dtype=bbtype)
TypeError: expected an object with a buffer interface
>>> b = np.array([(20,30),50],dtype=bbtype)
Traceback (most recent call last):
  File "<pyshell#563>", line 1, in <module>
    b = np.array([(20,30),50],dtype=bbtype)
TypeError: expected an object with a buffer interface
>>> bbtype = np.dtype([('f1', [('f2','i4'),('f3','i4')]),('f4','i4',(2,2))])
>>> b = np.array([(20,30),((1,2),(3,4)))],dtype=bbtype)
SyntaxError: invalid syntax
>>> b = np.array([(20,30),((1,2),(3,4))],dtype=bbtype)
Traceback (most recent call last):
  File "<pyshell#566>", line 1, in <module>
    b = np.array([(20,30),((1,2),(3,4))],dtype=bbtype)
TypeError: expected an object with a buffer interface
>>> dt = np.dtype([('name', '<U10'), ('grades', np.float64, (2,2))])
>>> 
>>> x = np.array([('Sarahdfefed', ((8.0, 7.0),(8.0, 7.0))), ('John', ((6.0, 7.0),(8.0, 7.0)))], dtype=dt)
>>> x
array([('Sarahdfefe', [[8.0, 7.0], [8.0, 7.0]]),
       ('John', [[6.0, 7.0], [8.0, 7.0]])], 
      dtype=[('name', '<U10'), ('grades', '<f8', (2, 2))])
>>> bbtype = np.dtype([('f1', [('f2','i4'),('f3','i4')]),('f4','i4',(2,2))])
>>> b = np.array([(20,30),((1,2),(3,4))],dtype=bbtype)
Traceback (most recent call last):
  File "<pyshell#572>", line 1, in <module>
    b = np.array([(20,30),((1,2),(3,4))],dtype=bbtype)
TypeError: expected an object with a buffer interface
>>> bbtype = np.dtype([('f1', 'i4'),('f4','i4',(2,2))])
>>> bbtype = np.dtype([('f1', [('f2','i4'),('f3','i4')]),('f4','i4',(2,2))])
>>> b = np.array([((20,30),((1,2),(3,4)))],dtype=bbtype)
>>> b
array([((20, 30), [[1, 2], [3, 4]])], 
      dtype=[('f1', [('f2', '<i4'), ('f3', '<i4')]), ('f4', '<i4', (2, 2))])
>>> b = np.array([((20,30),([1,2],[3,4]))],dtype=bbtype)
>>> b
array([((20, 30), [[1, 2], [3, 4]])], 
      dtype=[('f1', [('f2', '<i4'), ('f3', '<i4')]), ('f4', '<i4', (2, 2))])
>>> b = np.array([((20,30),[[1,2],[3,4]])],dtype=bbtype)
>>> b
array([((20, 30), [[1, 2], [3, 4]])], 
      dtype=[('f1', [('f2', '<i4'), ('f3', '<i4')]), ('f4', '<i4', (2, 2))])
>>> np.dtype([('f1', [('f2','i4'),('f3','i4')]),('f4','i4',2)])
dtype([('f1', [('f2', '<i4'), ('f3', '<i4')]), ('f4', '<i4', (2,))])

>>> b = np.array([((20,30),[1,2])],dtype=bbtype)
>>> b
array([((20, 30), [[1, 2], [1, 2]])], 
      dtype=[('f1', [('f2', '<i4'), ('f3', '<i4')]), ('f4', '<i4', (2, 2))])
>>> np.array([((20,30),[1,2])],dtype=bbtype)
array([((20, 30), [[1, 2], [1, 2]])], 
      dtype=[('f1', [('f2', '<i4'), ('f3', '<i4')]), ('f4', '<i4', (2, 2))])
>>> bbtype = np.dtype([('f1', [('f2','i4'),('f3','i4')]),('f4','i4',2)])
>>> b = np.array([((20,30),[1,2])],dtype=bbtype)
>>> b
array([((20, 30), [1, 2])], 
      dtype=[('f1', [('f2', '<i4'), ('f3', '<i4')]), ('f4', '<i4', (2,))])
>>> bbtype = np.dtype([('f1', [('f2','i4'),('f3','i4',2)]),('f4','i4',2)])
>>> b = np.array([((10,[1,2]),[10,20]),],dtype=bbtype)
>>> b
array([((10, [1, 2]), [10, 20])], 
      dtype=[('f1', [('f2', '<i4'), ('f3', '<i4', (2,))]), ('f4', '<i4', (2,))])
>>> a = np.array([[0,1,2],[3,4,5],[6,7,8]], dtype=np.float32)
\
>>> a
array([[ 0.,  1.,  2.],
       [ 3.,  4.,  5.],
       [ 6.,  7.,  8.]], dtype=float32)
>>> a
array([[ 0.,  1.,  2.],
       [ 3.,  4.,  5.],
       [ 6.,  7.,  8.]], dtype=float32)
>>> b = a[::2,::2]
>>> b
array([[ 0.,  2.],
       [ 6.,  8.]], dtype=float32)
>>> a.strides
(12, 4)
>>> b.strides
(24, 8)
>>> b
array([[ 0.,  2.],
       [ 6.,  8.]], dtype=float32)
>>> a
array([[ 0.,  1.,  2.],
       [ 3.,  4.,  5.],
       [ 6.,  7.,  8.]], dtype=float32)
>>> b.tostring()
b'\x00\x00\x00\x00\x00\x00\x00@\x00\x00\xc0@\x00\x00\x00A'
>>> x = b.tostring()
>>> len(x)
16
>>> x = a.tostring()
>>> x
b'\x00\x00\x00\x00\x00\x00\x80?\x00\x00\x00@\x00\x00@@\x00\x00\x80@\x00\x00\xa0@\x00\x00\xc0@\x00\x00\xe0@\x00\x00\x00A'
>>> len(x)
36
>>> len(a)
3
>>> a.tolist()
[[0.0, 1.0, 2.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0]]
>>> x = np.linspace(0,2*np.pi,10)
>>> x
array([ 0.        ,  0.6981317 ,  1.3962634 ,  2.0943951 ,  2.7925268 ,
        3.4906585 ,  4.1887902 ,  4.88692191,  5.58505361,  6.28318531])
>>> len(x)
10
>>> x[np.array([1,1,1])]
array([ 0.6981317,  0.6981317,  0.6981317])
>>> xx = np.arange(5,0,-1)
>>> xx
array([5, 4, 3, 2, 1])
>>> xx
array([5, 4, 3, 2, 1])
>>> xx[np.arange(True,False)]
array([], dtype=int32)
>>> xx
array([5, 4, 3, 2, 1])
>>> xx[np.arange(True,False,True,False,False)]
Traceback (most recent call last):
  File "<pyshell#617>", line 1, in <module>
    xx[np.arange(True,False,True,False,False)]
TypeError: function takes at most 4 arguments (5 given)
>>> xx[np.arange([True,False,True,False,False])]
Traceback (most recent call last):
  File "<pyshell#618>", line 1, in <module>
    xx[np.arange([True,False,True,False,False])]
TypeError: unsupported operand type(s) for -: 'list' and 'int'
>>> xx[np.array([True,False,True,False,False])]
array([5, 3])
>>> xx
array([5, 4, 3, 2, 1])
>>> xx[np.array([True,False])]
array([5])
>>> xx[np.array([True,False])][0] = 10
>>> xx
array([5, 4, 3, 2, 1])
>>> xx[[True,False]][0] = -5
>>> xx
array([5, 4, 3, 2, 1])
>>> yy = xx[[True,False]]
>>> 
>>> yy
array([4, 5])
>>> yy = xx[[True,False,True,False,False]]
>>> yy
array([4, 5, 4, 5, 5])
>>> xx[[True,False,True,False,False]]
array([4, 5, 4, 5, 5])
>>> xx
array([5, 4, 3, 2, 1])
>>> xx[np.array([True,False])] = -5
>>> xx
array([-5,  4,  3,  2,  1])
>>> xx[np.array([True,False])][0]
-5
>>> xx[[1,2]]
array([4, 3])
>>> xx[np.array([0,1,1,0,1])]
array([-5,  4,  4, -5,  4])
>>> xx
array([-5,  4,  3,  2,  1])
>>> xx[np.array([False,True,True,False,True])]
array([4, 3, 1])
>>> xx
array([-5,  4,  3,  2,  1])
>>> yy = xx[np.array([False,True,True,False,True])]
>>> yy
array([4, 3, 1])
>>> yy = -4,-3,-1
>>> xx
array([-5,  4,  3,  2,  1])
>>> yy
(-4, -3, -1)
>>> x[[3,5,1]]
array([ 2.0943951,  3.4906585,  0.6981317])
>>> x
array([ 0.        ,  0.6981317 ,  1.3962634 ,  2.0943951 ,  2.7925268 ,
        3.4906585 ,  4.1887902 ,  4.88692191,  5.58505361,  6.28318531])
>>> yy = x[[3,5,1]]
>>> yy
array([ 2.0943951,  3.4906585,  0.6981317])
>>> yy[0] = 5
>>> xx
array([-5,  4,  3,  2,  1])
>>> x
array([ 0.        ,  0.6981317 ,  1.3962634 ,  2.0943951 ,  2.7925268 ,
        3.4906585 ,  4.1887902 ,  4.88692191,  5.58505361,  6.28318531])
>>> yy
array([ 5.       ,  3.4906585,  0.6981317])
>>> yy = x[2:4]
>>> yy[0] = 5
>>> x
array([ 0.        ,  0.6981317 ,  5.        ,  2.0943951 ,  2.7925268 ,
        3.4906585 ,  4.1887902 ,  4.88692191,  5.58505361,  6.28318531])
>>> import random
>>> 
