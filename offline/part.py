import json

from . import core
from .unit import Unit

run_here = core.run_here()

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
	
	def get_unit(self, *units):
		unit_list = []
		
		for unit_name in units:
			#Error promotion information
			if type(unit_name) == int and unit_name > len(self.units):
				print(f'Unit number out of range, max number: {len(self.units)}')
				return
			elif type(unit_name) == str and unit_name not in self.units:
				print(f'Invalid unit name: {unit_name}\n\tValid unit list:')
				
				for i in range(len(self.units)):
					print(f'\t\t{i+1}.{self.units[i]}')
				
				return
			elif type(unit_name) != int and type(unit_name) != str:
				print('Only allow use int or str to represent unit name')
				return
			
			#Support use int instead unit's name
			if type(unit_name) == int:
				unit_name = self.units[unit_name - 1]
			
			try: #Try get unit_data from cache
				run_here.start()
				with open(f'cache/data/{self.file_name}_{self.name}_{unit_name}.json', encoding = 'UTF-8') as unit_file:
					unit_data = json.load(unit_file)
				run_here.end()
			except FileNotFoundError: #If don't have cache, get unit_data from self.data and create cache
				if type(self.data) == dict:
					unit_data = self.data[unit_name]
				elif type(self.data) == list:
					unit_data = self.data[self.units.index(unit_name)]
				
				run_here.start()
				with open(f'cache/data/{self.file_name}_{self.name}_{unit_name}.json', 'w', encoding = 'UTF-8') as unit_file:
					json.dump(unit_data, unit_file, indent = '\t', ensure_ascii = False)
				run_here.end()
			
			#create Unit and append to unit_list
			unit = Unit(self.file_name, self.name, unit_name, unit_data)
			unit_list.append(unit)
		
		#len == 0 -> impossible
		if len(unit_list) == 1: #If len == 1 -> only request one unit's data -> return Unit
			return unit_list[0]
		else: # If len > 1 -> request multi unit's data -> return list-Unit
			return unit_list