class StructField:
	def __init__(self,myformat,offset):
		self.format = myformat
		self.offset = offset
	def __get__(self,instance,cls):
		if instance is None:
			return self
		else:
			r  = struct.unpack_from(self.format,instance._buffer,self.offset)
			return r[0] if len(r) == 1 else r

			
class NestedStruct:
	def __init__(self,name,struct_type,offset):
		self.name = name
		self.struct_type = struct_type
		self.offset = offset
	def __get__(self,instance,cls):
		if instance is None:
			return self
		else:
			data = instance._buffer[self.offset:
					self.offset+self.struct_type.struct_size]
			result = self.struct_type(data)
			setattr(instance,self.name,result)
			return result

class StructureMeta(type):
	def __init__(self,clsname,bases,clsdict):
		fields = getattr(self,'_fields_',[])
		byte_order = ''
		offset = 0
		for myformat,fieldname in fields:
			if isinstance(myformat,StructureMeta):
				setattr(self,fieldname,
					NestedStruct(fieldname,myformat,offset))
				offset = myformat.struct_size
			else:
				if myformat.startswith(('<','>','!','@')):
					byte_order = myformat[0]
					myformat = myformat[1:]
				myformat = byte_order + myformat
				setattr(self,fieldname,StructField(myformat, offset))
				offset += struct.calcsize(myformat)
			setattr(self,'struct_size',offset)

			
class Structure(metaclass=StructureMeta):
	def __init__(self,bytedata):
		self._buffer = bytedata
	@classmethod
	def from_file(cls,f):
		return cls(f.read(cls.struct_size))

class SizedRecord:
	def __init__(self,bytedata):
		self._buffer = memoryview(bytedata)
	@classmethod
	def from_file(cls,f,size_fmt,include_size=False):
		sz_nbytes = struct.calcsize(size_fmt)
		sz_bytes = f.read(sz_nbytes)
		sz, = struct.unpack(size_fmt,sz_bytes)
		buf = f.read(sz-include_size*sz_nbytes)
		return cls(buf)
	def iter_as(self,code):
		if isinstance(code,str):
			s = struct.Struct(code)
			for off in range(0,len(self._buffer),s.size):
				yield s.unpack_from(self._buffer,off)
		elif isinstance(code,StructureMeta):
			size = code.struct_size
			for off in range(0,len(self._buffer),size):
				data = self._buffer[off:off+size]
				yield code(data)
		
class Point(Structure):
    _fields_ = [
          ('<d', 'x'),
          ('d', 'y')
    ]
	
class PolyHeader(Structure):
    _fields_ = [
          ('<i', 'file_code'),
          (Point, 'min'),         # nested struct
          (Point, 'max'),         # nested struct
          ('i', 'num_polys')
    ]
	
