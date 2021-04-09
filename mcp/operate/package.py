from ..source_file import raw_source_data

__all__ = [
	'package_source_version'
]

def package_source_version():
	return raw_source_data['game']['meta']['buildVersion']