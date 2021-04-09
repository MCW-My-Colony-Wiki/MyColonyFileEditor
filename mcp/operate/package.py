from ..source import Source

__all__ = [
	'package_source_version'
]

def package_source_version():
	return Source('game').data['meta']['buildVersion']