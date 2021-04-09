__all__ = [
    "class_name"
]

def class_name(obj):
	#type
	if obj is type:
		return obj.__class__.__name__
	#str, list, tuple, dict, ......
	if type(obj) is type:
		return obj().__class__.__name__
	#custom class
	return obj.__class__.__name__
