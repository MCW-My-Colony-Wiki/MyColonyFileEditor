from .category import Category
from .exceptions import raise_TpE, raise_ISE, raise_ICE
from .source_file import source_files, source_data
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
		if name not in source_files:
			raise_ISE(name)
		
		self.name = name
		self.data = source_data[name]
		self.dict = {name: Category(self, name) for name in self.data.keys()}
		self.list = list(self.dict.values())
		self.categories = list(self.dict.keys())
	
	def __getitem__(self, num):
		try:
			return self.list[num]
		except IndexError:
			raise StopIteration
	
	def __str__(self):
		return str(self.categories)
	
	def __repr__(self):
		return str(self.categories)
	
	def __len__(self):
		return len(self.categories)
	
	def category(self, name):
		try:
			return self.dict[name]
		except KeyError:
			raise_ICE(name)
