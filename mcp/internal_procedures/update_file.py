import requests
import os

from .get_version import get_latest_game_version, get_pack_game_version, get_game_file_version
from ..tools import run_here
from ..operate.package import load_config

config_data = load_config()

__all__ = [
	'update_game_file',
	'update_pack_game_version'
]

@run_here
def update_game_file(file):
	baseurl = 'https://www.apewebapps.com/apps/my-colony/{version}/{file}.js'
	page = requests.get(baseurl.format(version = get_latest_game_version(), file = file), timeout = config_data['timeout'])
	page.encoding = 'UTF-8'
	os.chdir('..')
	
	with open(f'source/{file}.js', 'w') as file:
		file.write(page.text)

@run_here
def update_pack_game_version():
	if get_pack_game_version() != get_game_file_version():
		os.chdir('..')
		with open('pack_info.json') as pi:
			pack_info = json.load(pi)
		
		pack_info['game_version'] = get_game_file_version()
		
		with open('pack_info.json', 'w') as pi:
			json.dump(pack_info, pi, indent = '\t', ensure_ascii = False)
