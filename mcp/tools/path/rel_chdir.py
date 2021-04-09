from os import chdir

__all__ = [
	'rel_chdir'
]

def rel_chdir(path):
	def cd_out(layer):
		while layer > 1:
			chdir('..')
			layer -= 1
	
	if path.startswith('...'):
		if '/' in path:
			layer, path = path.split('/', 1)
			cd_out(len(layer))
			chdir(path)
		else:
			cd_out(len(path))
	else:
		chdir(path)
