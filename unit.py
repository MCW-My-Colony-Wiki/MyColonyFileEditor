import json

class Unit():
	def __init__(self, part, unit_name, content):
		self.part = part #for reverse get part
		self.file = part.file #for reverse get game_file and alias of part.game_file
		self.name = unit_name #thinking usage
		self.raw = json.dumps(content, indent = '\t') #type(self.raw) -> str
		self.data = content #type(self.data) -> dict, str or list
	
	def __repr__(self):
		return self.raw
	
	def __str__(self):
		return self.raw
	
	def __len__(self):
		return len(self.raw)