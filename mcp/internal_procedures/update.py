from .self_check import get_version_number, download_source

from ..operate.package import get_package_source_version
from ..config import load_config

__all__ = [
	'check_update'
]

config_data = load_config()

def check_update(auto_update = False):
	version_number = get_version_number()
	package_source_version = get_package_source_version()
	
	if version_number[config_data['update_from']] != package_source_version:
		if not auto_update:
			do_update = input("[mcp][check_update] The package source files has been updated. Do you want to update now?(Enter 'Y' or 'y' to update, other input will be ignored and skip update)\n> ")
			true_like = ['Y', 'y']
			
			if do_update in true_like:
				download_source('game', 'strings')
		else:
			download_source('game', 'strings')
	else:
		pass
