from ..category import Game_file
from ..tools import run_here, format_game_file

__all__ = [
	'game',
	'strings'
]

@run_here
def get_file_data(file):
	with open(f'{file}.js', 'r', encoding = 'UTF-8') as game_file:
		data = format_game_file(game_file.read())
		return data

game = Game_file('game', get_file_data('game'))
strings = Game_file('strings', get_file_data('strings'))