from ..source import Source, Category, ListUnit
from ..exceptions import raise_TpE, raise_IUE

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

def getunit(para0, para1, para2 = None):
	'''
	'''
	def get_unit():
		if unit in cat:
			if type(cat.data) is ListUnit:
				return cat[cat.units.index(unit)]
			if type(cat.data) is dict:
				return cat.data[unit]
			if type(cat.data) is list:
				return cat[cat.index(unit)]
		raise_IUE(unit)
	
	#category check and get cat
	if type(para2) is str:
		cat = getcat(para0, para1)
		unit = para2
		return get_unit()
	if not para2:
		cat = para0
		unit = para1
		
		if isinstance(cat, Category):
			return get_unit()
		raise TypeError('if the last parameter is None, first parameter must be Category')
	raise_TpE('last parameter', [None, str])
