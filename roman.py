#coding=utf-8
__author__ = 'huanglibo'

import re
import os
import mock
import nose
import toobox

romanNumeralMap = (('M',  1000),
                   ('CM', 900),
                   ('D',  500),
                   ('CD', 400),
                   ('C',  100),
                   ('XC', 90),
                   ('L',  50),
                   ('XL', 40),
                   ('X',  10),
                   ('IX', 9),
                   ('V',  5),
                   ('IV', 4),
                   ('I',  1))


romanNumeralPattern = re.compile('''
	^				    # beginning of string
	M{0,3}			    # thousands - 0 to 4 M's
	(CM|CD|D?C{0,3})	# hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
						#			or 500-800 (D, followed by 0 to 3 C's)
	(XC|XL|L?X{0,3})	# tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
						#		or 50-80 (L, followed by 0 to 3 X's)
	(IX|IV|V?I{0,3})	# ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
						#		or 5-8 (V, followed by 0 to 3 I's)
	$				    # end of string
	''' ,re.X)


class RomanError(Exception): pass


class OutOfRangeError(RomanError): pass


class NotIntegerError(RomanError): pass


class InvalidRomanNumeralError(RomanError): pass


def toRoman(n):
    if not isinstance(n,int):
        raise NotIntegerError,"non-integers can not be converted"
    if not (0 < n < 4000):
        raise OutOfRangeError,"number out of range(must be 1...3999"

    result = ""
    for numeral, integer in romanNumeralMap:
        while n >= integer:
            result += numeral
            n -= integer
    return result

def fromRoman(s):
    if not s:
        raise InvalidRomanNumeralError,'Input can not be blank'
    if not romanNumeralPattern.search(s):
        raise InvalidRomanNumeralError, 'Invalid Roman numeral: %s' % s

    result = 0
    index = 0
    for numeral, integer in romanNumeralMap:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)

    return result


class RemovalService(object):
    def __init__(self):
        print "in init"
    def rm(self,filename):
        if os.path.isfile(filename):
            os.remove(filename)

class UploadService(object):
    def __init__(self,removal_service):
        self.removal_service = removal_service

    def upload_complete(self,filename):
        self.removal_service.rm(filename)

class Foo(object):
    @property
    def foo(self):
        return 'something'
    @foo.setter
    def foo(self,value):
        print value

def test():
    with mock.patch("__main__.Foo.foo",new_callable = mock.PropertyMock) as mock_foo:
        print type(mock_foo)
        mock_foo.return_value = 'mockity-mock'
        this_foo = Foo()
        print this_foo.foo
        this_foo.foo = 4
        print this_foo.foo

if __name__ == "__main__":
    maybar = toobox.Bar()