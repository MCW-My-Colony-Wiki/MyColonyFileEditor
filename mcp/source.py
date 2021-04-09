from .exceptions import raise_TpE, raise_ISE

from .tools.data.source_data import source_data

__all__ = [
	'Source'
]

source_files = [
	'game',
	'strings'
]

#Pre-created source file data
source_file_data = {name: source_data(name) for name in source_files}

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
	"""
	def __init__(self, name):
		if type(name) != str:
			raise_TpE('name', str)
		if name not in source_files:
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
