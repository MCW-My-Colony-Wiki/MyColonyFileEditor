from ..source_file import source_data

__all__ = [
	'package_source_version'
]

def package_source_version():
	return source_data['game']['meta']['buildVersion']