import json
from .unit import Unit

class Part():
	def __init__(self, game_file, part_name, content):
		self.file = game_file #for reverse get file
		self.name = part_name #thinking usage
		self.raw = json.dumps(content, indent = '\t') #type(self.raw) -> str
		self.data = content #type(self.data) -> dict, list or list-dict
		self.units = [] #type(self.units) -> list-unit
		
		if type(content) == dict: #contain single or multi layer dict
			units = list(content.keys())
			
			for unit_name in units:
				unit = Unit(self, unit_name, self.data[unit_name])
				self.units.append(unit)
		
		elif type(content) == list: #contain list or list-dict
			if type(content[0]) == dict and 'name' in content[0].keys(): #for list-dict
				for i in range(len(content)):
					unit_name = content[i]['name'].replace(' ', '_').replace("'", '')
					unit = Unit(self, unit_name, content[i])
					self.units.append(unit)
			
			else: #for list
				self.units = content
	
	def __repr__(self):
		return self.raw
	
	def __str__(self):
		return self.raw
	
	def __len__(self):
		return len(self.raw)