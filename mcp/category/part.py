import json

__all__ = [
	'Part'
]

class Part():
	def __init__(self, file_name, part_name, content):
		self.file_name = file_name #type(self.file_name) -> str | usage: set unit's file_name
		self.name = part_name #type(self.name) -> str | usage: set unit's part_name
		self.raw = json.dumps(content, indent = '\t', ensure_ascii = False) #type(self.raw) -> str | self.data's str format
		self.data = content #type(self.data) -> dict, list or list-dict | self.raw's dict, list or list-dict format
		self.units = [] #type(self.units) -> list-unit | a list of all unit's name
		
		if type(self.data) == dict: #contain single or multi layer dict
			self.units = list(self.data.keys())
		elif type(self.data) == list: #contain list or list-dict
			if type(self.data[0]) == dict and ('name' in self.data[0].keys() or 'title' in self.data[0].keys()): #for list-dict
				for i in range(len(self.data)):
					unit_name = self.data[i]['name'].replace(' ', '_').replace("'", '')
					self.units.append(unit_name)
			else: #for list
				self.units = content
	
	def __repr__(self):
		return self.raw
	
	def __str__(self):
		return self.raw
	
	def __len__(self):
		return len(self.units)
