import json

__all__ = [
	'Game_file'
]

class Game_file():
	def __init__(self, name, content):
		self.file_name = name #name of this file
		self.raw = content #type(self.raw) -> str
		self.data = json.loads(content) #type(self.data) -> dict
		self.parts = list(self.data.keys()) #type(self.parts) -> list-part
		
	def __repr__(self):
		return self.raw
	
	def __str__(self):
		return self.raw
	
	def __len__(self):
		return len(self.parts)
