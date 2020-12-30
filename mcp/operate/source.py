from ..source import Source, Category

__all__ = [
	'getsource',
	'getcat',
	'getunit',
]

def getsource(source):
	'''
	'''
	return Source(source)

def getcat(source, category):
	'''
	'''
	if type(source) is str:
		source = getsource(source)
	
	return Category(source, category)

def getunit(category, unit, source = None):
	'''
	'''
	pass
