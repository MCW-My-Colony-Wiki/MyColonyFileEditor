from ..source import Source
from ..category import Category, ListUnit

from ..tools.data.asgmt_brench import asgmt_brench

__all__ = [
	'source',
	'category',
	'unit',
]

def source(file):
	'''
	'''
	return Source(file)

def category(source, name):
	'''
	'''
	return Category(source, name)

def unit(source, category, name):
	if not isinstance(category, Category):
		category = Category(source, category)
	
	return eval(asgmt_brench(category.data, '', {
		"ListUnit": "category[category.units.index(name)]",
		"dict": "category.data[name]",
		"list": "category[category.index(name)]"
		}))
