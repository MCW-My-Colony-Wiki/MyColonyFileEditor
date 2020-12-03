import json

from .core import converter, run_here
from .part import Part

__all__ = [
	'strings',
	'game'
]

run_here = run_here()

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
	
	def get_part(self, *parts):
		part_list = []
		
		for part_name in parts:
			#Error promotion information
			if type(part_name) == int and part_name > len(self.parts):
				print(f'Part number out of range, max number: {len(self.parts)}')
				return
			elif type(part_name) == str and part_name not in self.parts:
				print(f'Invalid part name: {part_name}\n\tValid part list:')
				
				for i in range(len(self.parts)):
					print(f'\t\t{i+1}.{self.parts[i]}')
				
				return
			elif type(part_name) != int and type(part_name) != str:
				print('Only allow use int or str to represent part name')
				return
			
			#Support use int instead part's name
			if type(part_name) == int:
				part_name = self.parts[part_name - 1]
			
			try: #Try get part_data from cache
				run_here.start()
				with open(f'cache/data/{self.file_name}_{part_name}.json', encoding = 'UTF-8') as part_file:
					part_data = json.load(part_file)
				run_here.end()
			except FileNotFoundError: #If don't have cache, get part_data from self.data and create cache
				part_data = self.data[part_name]
				
				run_here.start()
				with open(f'cache/data/{self.file_name}_{part_name}.json', 'w', encoding = 'UTF-8') as part_file:
					json.dump(part_data, part_file, indent = '\t', ensure_ascii = False)
				run_here.end()
			
			#create Part and append to part_list
			part = Part(self.file_name, part_name, part_data)
			part_list.append(part)
		
		#len == 0 -> impossible
		if len(part_list) == 1: #If len == 1 -> only request one part's data -> return Part
			return part_list[0]
		else: # If len > 1 -> request multi part's data -> return list-Part
			return part_list

run_here.start()
strings_data = converter('game_file/strings.js')
game_data = converter('game_file/game.js')
run_here.end()

strings = Game_file('strings', strings_data)
game = Game_file('game', game_data)