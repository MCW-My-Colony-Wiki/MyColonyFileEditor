from ..source import *

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
	if type(source) == str:
		source = getsource(source)
	
	return Category(source, category)

def getunit(category, unit, source = None):
	'''
	'''
	pass
