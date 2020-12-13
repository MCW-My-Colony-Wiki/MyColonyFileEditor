from .config import _load_config, config
from .check_update import check_update, del_cache

__all__ = [
	'config',
	'check_update',
	'del_cache'
]

_config_data = _load_config()
if _config_data['check_update']:
	check_update()

from .get_part import *
from .get_unit import *