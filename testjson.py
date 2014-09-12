#import json_myobj
import json

#obj = json_myobj.MyObj("instance")
序列化python对象
def serialize_instance(obj):
	d = {'__class__':obj.__class__.__name__,
		'__module__':obj.__module__,
		}
	d.update(obj.__dict__)
	return d
	
#d = serialize_instance(obj)
#json.dumps(obj,default=serialize_instance)

encoded_object = '[{"s": "instance value goes here", "__module__": "json_myobj", "__class__": "MyObj"},{"10":10}]'

def unserialize_object(d):
	if "__class__" in d :
		class_name = d.pop('__class__')
		module_name = d.pop('__module__')
		module = __import__(module_name)
		print "module:",module
		_class = getattr(module,class_name)
		print "class:",_class
		args = dict((key,value) for key, value in d.items())
		print "args:",args
		inst = _class(**args)
	else:
		inst = d
	return inst

d = {"s": "instance value goes here", "__module__": "json_myobj", "__class__": "MyObj"}

#myobj = unserialize_object(d)
x = json.loads(encoded_object,object_hook=unserialize_object)
print x


