import os,struct,os.path,mmap,tempfile
import traceback
import atexit
hexstr = lambda s:map(lambda c:hex(ord(c)),s)

def cleanup(handle):
	print "in cleanup"
	print handle._file.name
	print handle._file_name
	if handle._mem :
		print "in cleanup mem"
		handle._mem.close()
	if handle._file:
		print "in cleanup file"
		bsize = handle._realsize * handle._item_size
		handle._file.truncate(bsize)
		handle._file.close()
	if handle._file_name:
		print "handle._file:",handle._file_name
		os.remove(handle._file_name)
	
class Memarray(object):
	_file = _mem = None
	_realsize = _capsize = 0
	def __init__(self,item_type='B',file_name=None,capsize = 1024*1024):
		self._item_size = struct.calcsize(item_type)
		if not file_name:
			self._fileno,self._file_name = tempfile.mkstemp(suffix="-array",prefix="mem-")
			#self._file = open(self._file_name,'w+')
			self._file = os.fdopen(self._fileno,'w+')
			self._enlarge(capsize)
		else:
			self.fromfile(file_name)
		atexit.register(cleanup, self)
		
	def fromfile(self,file_name):
		print "fromfile"
		self._file_name = None
		#	print "None"
		if not os.path.exists(file_name):
			print "the file %s is not exists" % file_name
			raise
		fsize = os.path.getsize(file_name)
		print "fsize:",fsize
		if fsize == 0:
			print "the size of %s is zero" % file_name
			raise
		if self._file : self._file.close()
		if self._mem : self._mem.close()
		self._file = open(file_name,"r+")
		self._realsize = self._capsize = fsize/self._item_size
		#bsize = self._realsize * self._item_size
		#self._file.truncate(bsize)
		self._mem = mmap.mmap(self._file.fileno(),fsize)
	def tofile(self,file_name):
		print "tofile"
		if file_name == self._file.name:
			print "the same"
			raise
		f = open(file_name,"w+")
		bsize = self._realsize * self._item_size
		f.write(self._mem[:bsize])
		f.close()
	def _enlarge(self,capsize):
		print "enlarge"
		if self._capsize >= capsize:
			return
		self._capsize = capsize
		self._file.seek(capsize*self._item_size-1)
		self._file.write('')
		self._file.flush()
		tell = self._file.tell()
		print "tell",tell
		if self._mem : self._mem.close()
		self._mem = mmap.mmap(self._file.fileno(),tell+1)
	def __getitem__(self,idx):
		print "__getitem__"
		if idx < 0 or idx > self._realsize:
			raise IndexError
		return self._access(idx)
	def __setitem__(self,idx,buf):
		print "__setitem__"
		if idx < 0 or idx > self._realsize:
			raise IndexError
		if isinstance(buf, str) or len(buf) != self._item_size:
			print "Not a string, or the buffer size is incorrect!"
			raise
		self._access(idx,buf)
	def _access(self,idx,buf=None):
		print "_access",self._realsize,self._capsize
		start = idx*self._item_size
		end = start+self._item_size
		if not buf:
			return self._mem[start:end]
		else:
			print "buf:",hexstr(buf)
			self._mem[start:end] = buf

	def __del__(self):
		print "in del"
		

	def size(self):
		return self._realsize
	def append(self,buf):
		print "in append"
		if not isinstance(buf, str) or len(buf) != self._item_size:
			print "Not a string, or the buffer size is incorrect!"
			raise
		if self._realsize >= self._capsize:
			self._enlarge(self._capsize * 2)
		print "a:",hexstr(buf)
		self._access(self._realsize,buf)
		self._realsize += 1
	def __iter__(self):
		print "in __iter__"
		for i in xrange(self._realsize):
			yield self._access(i)
	def truncate(self,tsize):
		print "in truncate"
		if self.__realsize > tsize:
			self.__realsize = tsize
			
mm = Memarray("2i",'E:\\code\\test\\a.txt')
#mm = Memarray("2i")
a = struct.pack('2i',10,10)
print "a:",hexstr(a)
print mm._realsize,mm._capsize
mm.append(a)
print mm._realsize,mm._capsize
print hexstr(mm[1])
