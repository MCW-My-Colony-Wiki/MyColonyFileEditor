from ..category import Game_file
from ..core import run_here, converter

__all__ = [
	'game',
	'strings'
]

@run_here
def get_file_data(file):
	with open(f'{file}.js', 'r', encoding = 'UTF-8') as game_file:
		data = converter(game_file.read())
		return data

game = Game_file('game', get_file_data('game'))
strings = Game_file('strings', get_file_data('strings'))