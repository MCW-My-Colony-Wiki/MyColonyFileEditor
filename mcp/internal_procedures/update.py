from .get_version import get_pack_game_version, get_latest_game_version
from .update_file import update_game_file, update_pack_game_version

from ..operate.package import load_config
from ..operate.unit import get_unit

__all__ = [
	'check_update',
	'update'
]

config_data = load_config()

def check_update():
	if config_data['show_update_process']:
		print('mcp check_update process')
		print('	Checking update...')

	pack_game_version = get_pack_game_version()
	latest_game_version = get_latest_game_version()
	
	if pack_game_version != latest_game_version:
		if config_data['show_update_process']:
			print('	Update founded, updating...')
		
		update_game_file('strings')
		update_game_file('game')
		
		if config_data['show_update_process']:
			print(f'	Update completed, from v{pack_game_version} update to v{latest_game_version}')
		
		update_pack_game_version()
	else:
		if config_data['show_update_process']:
			print(f'	Local game files have been updated to latest version(v{get_pack_game_version()})')

def update():.
	pass
