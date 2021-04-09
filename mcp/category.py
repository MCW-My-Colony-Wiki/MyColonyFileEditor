from .source import Source
from .units import VideoTutorial, Soundtrack, Map, Race, Civilization, Tile, Resource, Utility, Occupation, Terrain, Technology, Building, Vehicle

from .exceptions import raise_TpE, raise_ICE

from .tools.data.asgmt_brench import asgmt_brench

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
		
		self.category = eval(asgmt_brench(category, 'category', {"str": "Category('game', category)", "Category": "category"}))
		
		#set self.data
		try:
			unit_class = list_unit_cat[self.category.name]
			self.data = [unit_class(category, item) for item in data]
		except KeyError:
			#list
			for item in data:
				if type(item) is not dict:
					raise_TpE('item in data', dict)
			
			#list of dict that not add to list_unit_cat
			raise Warning(f"Category '{category.name}' is unavailable, please report this issue on github(https://github.com/Euxcbsks/mcp/issues)")
		
		self.units = [unit.name if hasattr(unit, 'name') else unit.title for unit in self.data]
	
	def __getitem__(self, num_of_unit):
		if num_of_unit < len(self.data):
			return self.data[num_of_unit]
		raise StopIteration
	
	def __contains__(self, unit):
		if isinstance(unit, Unit) or type(unit) is str:
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
		source = eval(asgmt_brench(source, 'source', {'str': "Source(source)", 'Source': "source"}))
		
		if name not in source.categories:
			raise_ICE(name)

		data = source.data[name]
		self.name = name
		self.source = source
		self.raw_data = data

		try:
			self.data = ListUnit(self, data)
			self.units = self.data.units
		except TypeError:
			self.keys = list(data.keys())
	
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
		if isinstance(item, Unit) or type(item) is str:
			return item in self.data
		return False
	
	def __str__(self):
		if hasattr(self, 'units'):
			return str(self.units)
		if hasattr(self, 'keys'):
			return str(self.keys)
		return str(self.data)
	
	def __repr__(self):
		self.__str__()
	
	def __len__(self):
		return len(self.data)
