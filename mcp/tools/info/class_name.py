__all__ = [
    "class_name"
]

def class_name(obj):
	if obj in {str, int, float, list, dict, set, tuple}:
		return obj.__name__
	return obj.__class__.__name__
