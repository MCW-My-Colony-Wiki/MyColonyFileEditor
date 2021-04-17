from .units import VideoTutorial, Soundtrack, Map, Race, Civilization, Tile, Resource, Utility, Occupation, Terrain, Technology, Building, Vehicle
from .source_file import source_data

from .exceptions import raise_TpE, raise_ICE, InvalidCategoryError

from .tools.data.asgmt_branch import asgmt_branch
from .tools.info.class_name import class_name
from .tools.data.format_attr import format_name

__all__ = [
	"Category"
]

list_unit_cat = {
	'videoTutorials': VideoTutorial,
	'soundtrack': Soundtrack,
	'mapTypes': Map,
	'races': Race,
	'civilizations': Civilization,
	'tiles': Tile,
	'resources': Resource,
	'utilities': Utility,
	'occupations': Occupation,
	'terrains': Terrain,
	'technology': Technology,
	'buildings': Building,
	'vehicles': Vehicle,
	'demands': None
}

def attr_branch(obj, branch):
	dir_obj = set(dir(obj))
	branch_key = set(branch.keys())
	
	return branch[list(dir_obj & branch_key)[0]]

class ListUnit:
	'''
	Internal class
	
	Argument
	--------
	- category
	  'Category' type, must in list_unit_cat
	- data
	  'list' type, list of units data
	'''
	def __init__(self, category, data):
		#use when create instance outside Category
		if not isinstance(category, Category):
			raise_TpE('category', Category)
		
		if type(data) is not list:
			raise_TpE('data', list)
		
		category_name = category.name
		
		if category_name not in list_unit_cat:
			raise InvalidCategoryError(f"[internal] '{category_name}' not in list_unit_cat, if this Error appear after My Colony update, please check the source file")
		
		try:
			#list[Unit]
			unit_class = list_unit_cat[category_name]
			
			#unit_class may be None
			if unit_class:
				self.data = data
				self.list = [unit_class(category, item) for item in data]
				self.units = [unit.name if hasattr(unit, 'name') else unit.title for unit in self.list]
				self.dict = dict(zip(self.units, self.list))
			else:
				self.data = data
				self.dict = {num: unit for num, unit in enumerate(data)}
				self.list = data
				self.units = data
		except KeyError:
			#list[item]
			raise_TpE('item in data', dict)
	
	def __getitem__(self, num):
		try:
			return self.list[num]
		except IndexError:
			raise StopIteration
	
	def __str__(self):
		return str(self.list)
	
	def __repr__(self):
		return str(self.list)
	
	def __len__(self):
		return len(self.list)

class Category:
	'''
	'''
	def __init__(self, source, name):
		#overwrite source by source data, if type(source) is "Source", it can reduce memory usege
		source = eval(asgmt_branch(source, 'type', {'str': "source_data[source]", 'Source': "source.data"}, obj_sig = 'source'))
		
		if name not in source:
			raise_ICE(name)
		
		#pre-create category data
		data = source[name]
		
		self.name = name
		self.data = data
		
		try:
			#list[Unit]
			#units may be None
			list_unit = ListUnit(self, data)
			branch = {
				"name": "unit.name",
				"title": "unit.title"
			}
			self.units = list_unit.units
			self.dict = {eval(asgmt_branch(unit, attr_branch, branch)) if hasattr(unit, 'name') or hasattr(unit, 'title') else num: unit for num, unit in enumerate(list_unit)}
			self.list = list(self.dict.values())
		except TypeError:
			#dict
			self.keys = list(data.keys())
			self.dict = data
			self.list = list(data.values())
		except InvalidCategoryError:
			#list[item]
			self.element = data
			self.dict = {num: item for num, item in enumerate(data)}
			self.list = data
	
	def __getitem__(self, num_of_item):
		#need support both list and dict
		if num_of_item < len(self.data):
			#list of str or list of unit
			try:
				return self.data[num_of_item]
			#dict
			except KeyError:
				return self.keys[num_of_item]
		else:
			raise StopIteration
	
	def __str__(self):
		return eval(asgmt_branch(self, attr_branch, {
			'units': 'str(self.units)',
			'keys': 'str(self.keys)',
			'element': 'str(self.element)'
		}))
	
	def __repr__(self):
		self.__str__()
	
	def __len__(self):
		return len(self.data)
