import os

from ..core import run_here

__all__ = [
	'del_cache',
	'del_pycache'
]

@run_here
def del_cache():
	cache_dire = '..cache'
	
	if cache_dire.startswith('..'):
		while cache_dire.startswith('..'):
			os.chdir('..')
			cache_dire = cache_dire[1:]
		cache_dire = cache_dire[1:]
	
	cache_listdir = os.listdir(cache_dire)
	
	def find_del_file(dire):
		listdir = os.listdir(dire)
		
		for path in listdir:
			dpath = f'{dire}/{path}'
			if os.path.isdir(dpath):
				find_file(dpath)
			elif os.path.isfile(dpath):
				os.remove(dpath)
	
	find_del_file(cache_dire)

@run_here
def del_pycache():
	os.chdir('..')
	print(os.getcwd())