from ..source import Source

__all__ = [
	'get_package_source_version'
]

def get_package_source_version():
	return Source('game').data['meta']['buildVersion']