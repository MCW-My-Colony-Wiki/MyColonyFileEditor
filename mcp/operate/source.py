from ..source import Source
from ..category import Category

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

def category(source_name, name):
	'''
	'''
	return Category(source_name, name)

def unit(source_name, category, name):
	if not isinstance(category, Category):
		category = Category(source_name, category)
	
	return eval(asgmt_brench(category.data, 'type', {
		"ListUnit": "category[category.units.index(name)]",
		"dict": "category.data[name]",
		"list": "category[category.index(name)]"
		}))
