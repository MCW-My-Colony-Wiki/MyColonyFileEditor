from .base import CommonBase

class CategoryBase(CommonBase):
	def __init__(self, file, name) -> None:
		self.file = file
		self.name = name
	
	def __getitem__(self, target):
		raise NotImplementedError("subclasses of CategoryBase must provide a __getitem__() method")
	
	def __iter__(self):
		raise NotImplementedError("subclasses of CategoryBase must provide a __iter__() method")
	
	def __repr__(self) -> str:
		return f"<File: {self.file}, Name: {self.name}>"
	
	def units(self):
		raise NotImplementedError("subclasses of CategoryBase must provide a units() method")
