#Self check
from .internal_procedures.self_check import *

#Load config
from .config import load_config, config
config_data = load_config()

#Check update
if config_data['auto_update'] or config_data['check_update']:
	from .internal_procedures.update import check_update
	check_update(config_data['auto_update'])

del load_config, config_data

from .operate.source import *

__all__ = [
	'check_update',
	'config',
	'operate',
	'getsource',
	'getcat',
	'getunit'
]
