from ..source import Source
from ..category import Category

from ..tools.data.asgmt_branch import asgmt_branch
from ..exceptions import InvalidSourceError, InvalidCategoryError, InvalidUnitError

__all__ = [
	'source',
	'category',
	'unit',
]

def source(file):
	'''
	'''
	try:
		return Source(file)
	except InvalidSourceError:
		raise InvalidSourceError(f"`file` must be 'game' or 'strings` not {file}")

def category(from_source, name):
	'''
	'''
	if type(from_source) is not Source:
		from_source = source(from_source)
	
	try:
		return Category(from_source, name)
	except InvalidCategoryError:
		raise InvalidCategoryError(f"'{name}' not in '{from_source}'")

def unit(from_category, name, source_name = None):
	if not isinstance(from_category, Category):
		if not source_name:
			raise ValueError("if type(from_category) is not Category, the source_name can't be None")
		
		from_category = category(source_name, from_category)
	
	try:
		return eval(asgmt_branch(from_category.data, 'type', {
			"ListUnit": "from_category[from_category.units.index(name)]",
			"dict": "from_category.data[name]",
			"list": "from_category[from_category.index(name)]"
			}))
	except InvalidUnitError:
		raise InvalidUnitError(f"'{name} not in '{from_category}'")
