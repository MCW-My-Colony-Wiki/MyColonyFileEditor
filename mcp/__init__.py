#Check indispensable file
from .internal_procedures.self_check import check_source

if not check_source():
	raise Warning('Missing file! Please try to reinstall this package to solve this problem')

del check_source

#Create config_data
from .config import load_config

config_data = load_config()

del load_config

#Check update
from .internal_procedures import check_update, update

if config_data['auto_update']:
	update()

if config_data['check_update']:
	check_update()

del config_data

#Import package operate
from .operate.package import config, del_cache

__all__ = [
	'update',
	'check_update',
	'config',
	'del_cache'
]
