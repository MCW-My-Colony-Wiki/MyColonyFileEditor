import os
import json

from ..tools import run_here, rel_chdir
from ..check import option_check

__all__ = [
	'del_cache',
	'del_pycache'
]

@run_here
def del_cache():
	rel_chdir('../cache')
	cache_listdir = os.listdir('.')
	
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
	pass