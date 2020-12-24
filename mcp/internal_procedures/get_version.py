import os
import json

from ..tools import run_here
from ..operate.config import load_config
from ..operate.unit import get_unit

__all__ = [
	'get_pack_game_version',
	'get_game_file_version'
]

config_data = load_config()

@run_here
def get_pack_game_version():
	os.chdir('..')
	with open('pack_info.json', 'r', encoding = 'UTF-8') as pi:
		pack_info = json.load(pi)
		pack_game_version = pack_info['game_version']
	return pack_game_version

@run_here
def get_game_file_version():
	game_file_version = get_unit('game', 'meta', 'buildVersion')
	return game_file_version
