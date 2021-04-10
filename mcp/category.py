from .units import VideoTutorial, Soundtrack, Map, Race, Civilization, Tile, Resource, Utility, Occupation, Terrain, Technology, Building, Vehicle
from .source_file import raw_source_data

from .exceptions import raise_TpE, raise_ICE

from .tools.data.asgmt_brench import asgmt_brench
from .tools.info.class_name import class_name
from .tools.data.format_attr import format_name

__all__ = [
	"ListUnit",
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

class ListUnit:
	def __init__(self, category, data):
		if type(data) is not list:
			raise_TpE('data', list)
		
		self.category = eval(asgmt_brench(category, 'type', {
			"str": "Category('game', category)",
			"Category": "category"
		}, obj_sig = 'category'))

		#set self.data, self.units
		try:
			unit_class = list_unit_cat[self.category.name]

			if unit_class:
				self.data = [unit_class(category, item) for item in data]
				self.units = [unit.name if hasattr(unit, 'name') else unit.title for unit in self.data]
			else:
				self.data = data
				self.units = data
		except KeyError:
			#list
			for item in data:
				if type(item) is not dict:
					raise_TpE('item in data', dict)
			
			#list of dict that not add to list_unit_cat
			raise Warning(f"Category '{category.name}' is unavailable, please report this issue on github(https://github.com/Euxcbsks/mcp/issues)")
		
	
	def __getitem__(self, num_of_unit):
		if num_of_unit < len(self.data):
			return self.data[num_of_unit]
		raise StopIteration
	
	def __contains__(self, unit):
		if class_name(unit) in {"Unit", "str"}:
			try:
				unit = unit.name
			except AttributeError:
				pass
			
			return format_name(unit) in self.units
		return False
	
	def __str__(self):
		return self.category.name
	
	def __repr__(self):
		self.__str__()
	
	def __len__(self):
		return len(self.units)

class Category:
	'''
	'''
	def __init__(self, source, name):
		source_data = eval(asgmt_brench(source, 'type', {'str': "raw_source_data[source]", 'Source': "source.raw_data"}, obj_sig = 'source'))
		
		if name not in source_data:
			raise_ICE(name)

		data = source_data[name]
		self.name = name
		self.raw_data = data
		self.source = source

		try:
			#ListUnit
			self.units = ListUnit(self, data)
		except TypeError:
			#dict or list
			exec(asgmt_brench(data, 'type', {
				"dict": "self.keys = list(data.keys())",
				"list": "self.element = data"
			}))
	
	def __getitem__(self, num_of_item):
		if num_of_item < len(self.data):
			#list of str or list of unit
			try:
				return self.data[num_of_item]
			#dict
			except KeyError:
				return self.keys[num_of_item]
		else:
			raise StopIteration
	
	def __contains__(self, item):
		if class_name(item) in {"Unit", "str"}:
			return item in self.data
		return False
	
	def __str__(self):
		if hasattr(self, 'units'):
			return str(self.units)
		if hasattr(self, 'keys'):
			return str(self.keys)
		return str(self.element)
	
	def __repr__(self):
		self.__str__()
	
	def __len__(self):
		return len(self.data)
