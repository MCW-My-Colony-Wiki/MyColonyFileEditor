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
		return len(self.raw)
	
	def get_part(self, *part):
		part_list = []
		
		for part_name in part:
			#Support use int instead part's name
			if type(part_name) == int and part_name <= len(self.parts):
				part_name = self.parts[part_name-1]
			
			#Error promotion information
			if part_name not in self.parts:
				print(f'Invalid part: {part_name}\n\tValid part list:')
				
				for i in range(len(self.parts)):
					print(f'\t\t{i+1}.{self.parts[i]}')
				
				return
			
			#Get part from cache or game_file and append it to part_list
			try:
				run_here.start()
				with open(f'cache/data/{self.file_name}_{part_name}.json', encoding = 'UTF-8') as part_file:
					part_data = json.load(part_file)
				run_here.end()
				
				part = Part(self, part_name, part_data)
				part_list.append(part)
			except FileNotFoundError:
				part_data = self.data[part_name]
				part = Part(self, part_name, part_data)
				
				run_here.start()
				with open(f'cache/data/{self.file_name}_{part_name}.json', 'w', encoding = 'UTF-8') as part_file:
					json.dump(part_data, part_file, indent = '\t')
				run_here.end()
				
				part_list.append(part)
		
		
		if len(part_list) == 1:
			return part_list[0]
		else:
			return part_list

run_here.start()
strings_data = converter('game_file/strings.js')
game_data = converter('game_file/game.js')
run_here.end()

strings = Game_file('strings', strings_data)
game = Game_file('game', game_data)