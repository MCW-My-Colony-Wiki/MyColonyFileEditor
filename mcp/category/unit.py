import json

__all__ = [
	'Unit'
]

class Unit():
	def __init__(self, file_name, part_name, unit_name, content):
		self.file_name = file_name #type(self.file_name) -> str
		self.part_name = part_name #type(self.part_name) -> str
		self.name = unit_name #type(self.name) -> str
		self.raw = json.dumps(content, indent = '\t', ensure_ascii = False) #type(self.raw) -> str | self.data's str format
		self.data = content #type(self.data) -> dict, str or list | self.raw's dict, str or list format
	
	def __repr__(self):
		return self.raw
	
	def __str__(self):
		return self.raw
	
	def __len__(self):
		return len(self.raw)