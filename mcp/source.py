from .exceptions import raise_TpE, raise_ISE, raise_ICE, raise_IUE
from .tools.data import source_data, format_name

__all__ = [
	##Base class
	'Source',
	'Category',
	'Unit',
	#Base on Unit
	'VideoTutorial',
	'Soundtrack',
	'Map',
	'Race',
	'Civilization',
	'Tile',
	'Resource',
	'Utility',
	'Occupation',
	'Terrain',
	'Technology',
	'Building',
	'Vehicle'
]

source_file_list = [
	'game',
	'strings'
]

#pre-created data
source_file_data = {name: source_data(name) for name in source_file_list}

#pre-filter out type(data) == list of dict
cat_to_unit_dict = {
	'videoTutorials': 'VideoTutorial',
	'soundtrack': 'Soundtrack',
	'mapTypes': 'Map',
	'races': 'Race',
	'civilizations': 'Civilization',
	'tiles': 'Tile',
	'resources': 'Resource',
	'utilities': 'Utility',
	'occupations': 'Occupation',
	'terrains': 'Terrain',
	'technology': 'Technology',
	'buildings': 'Building',
	'vehicles': 'Vehicle'
}

#variants of built-in type
class ListUnit:
	def __init__(self, category, data):
		#category check
		if isinstance(category, Category):
			pass
		else:
			raise_TpE('category', Category)
		
		#data check
		if type(data) is list:
			#get unit(class)
			try:
				unit_class = eval(cat_to_unit_dict[category.name])
			except KeyError:
				#list
				for item in data:
					if type(item) != dict:
						raise_TpE('item in data', dict)
				#list of dict that not add to cat_to_unit_dict
				raise Warning(f"""Category '{category.name}' is temporarily unavailable, please report this issue to the developer on github.
Report issue here: https://github.com/Euxcbsks/mcp/issues

If you are a developer, please check source/game.js changes""")
		else:
			raise_TpE('data', list)
		
		self.data = [unit_class(category, item) for item in data]
		self.units = [str(unit) for unit in self.data]
	
	def __len__(self):
		return len(self.units)

#Custom base class
class Source:
	"""Content all data in specified source file
	
	Usage
	-----------
	- Create instance ::
		
		source = Source(source_file_name)
	
	'source_file_name' must be 'game' or 'strings'
	
	- for loop
		.. code-block:: python3
			
			for cate in Source:
				print(cate.name)
	
	'cate' is a `Category`
	
	Attributes
	-----------
	- name: name of this source file
	- data: all data in this source file
	- categories: all category in this source file
	
	Method
	-----------
	
	"""
	def __init__(self, name):
		#name check
		if type(name) != str:
			raise_TpE('name', str)
		if name not in source_file_list:
			raise_ISE(name)
		
		self.name = name
		self.data = source_file_data[name]
		self.categories = list(self.data.keys())
	
	def __getitem__(self, num_of_cat):
		if num_of_cat < len(self.categories):
			cat_name = self.categories[num_of_cat]
			return Category(self, cat_name)
		raise StopIteration
	
	def __contains__(self, category):
		if isinstance(category, Category) or type(category) is str:
			try:
				category = category.name
			except AttributeError:
				pass
			
			return category in self.data
		return False
	
	def __str__(self):
		return str(self.categories)
	
	def __repr__(self):
		self.__str__()
	
	def __len__(self):
		return len(self.categories)

class Category:
	'''
	'''
	def __init__(self, source, name):
		#source check
		if isinstance(source, Source):
			self.source = source
		else:
			raise_TpE('source', Source)
		
		#name check
		if name in source.categories:
			self.name = name
		else:
			raise_ICE(name)
		
		#type(data) may be list(may contain dict) or dict
		data = source.data[name]
		
		#list or list of dict
		if type(data) is list:
			#list of dict
			try:
				data = ListUnit(self, data)
				self.units = data.units
			#list
			except TypeError:
				pass
		#dict
		else:
			self.keys = list(data.keys())
		
		self.data = data
	
	def __getitem__(self, num_of_item):
		if num_of_item < len(self.data):
			pass
		else:
			raise StopIteration
	
	def __str__(self):
		if hasattr(self, 'units'):
			return self.units
		if hasattr(self, 'keys'):
			return self.keys
		return self.name
	
	def __repr__(self):
		self.__str__()

class Unit:
	def __init__(self, category, data):
		if isinstance(category, Category):
			self.source = category.source
			self.category = category
		else:
			raise_TpE('category', Category)
		
		if type(data) is dict:
			self.data = data
		else:
			raise_TpE('data', dict)

#Base on Unit
class VideoTutorial(Unit):
	pass

class Soundtrack(Unit):
	pass

class Map(Unit):
	pass

class Race(Unit):
	pass

class Civilization(Unit):
	pass

class Tile(Unit):
	pass

class Resource(Unit):
	pass

class Utility(Unit):
	pass

class Occupation(Unit):
	pass

class Terrain(Unit):
	pass

class Technology(Unit):
	pass

class Building(Unit):
	def __init__(self, category, data):
		super().__init__(category, data)
		
		self.name = format_name(self.data['name'])
		self.rname = self.data['name']
	
	def __str__(self):
		return self.name

class Vehicle(Unit):
	pass
