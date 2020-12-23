from .internal_procedures import *
from .config import load_config, config
from .operate.package import *

__all__ = [
	'config',
	'check_update',
	'del_cache'
]

config_data = load_config()
del load_config

if config_data['check_update']:
	check_update()
del config_data
