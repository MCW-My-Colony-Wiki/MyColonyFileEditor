from .category import Category
from .exceptions import raise_TpE, raise_ISE
from .source_file import source_files, raw_source_data
from .tools.info.class_name import class_name

__all__ = [
	'Source'
]

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
		self.raw_data = raw_source_data[name]
		self.categories = [Category(self, category) for category in self.raw_data.keys()]
	
	def __getitem__(self, cat_num):
		if cat_num < len(self.categories):
			return self.categories[cat_num]
		raise StopIteration
	
	def __contains__(self, category):
		if class_name(category) in {'Category', 'str'}:
			try:
				category = category.name
			except AttributeError:
				pass
			
			return category in self.data
		return False
	
	def __str__(self):
		return str(self.categories)
	
	def __repr__(self):
		return str(self.categories)
	
	def __len__(self):
		return len(self.categories)
