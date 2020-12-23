import os
import json

from ..tools import run_here, rel_chdir
from ..check import option_check

__all__ = [
	'load_config'
	'config'
	'del_cache',
	'del_pycache'
]

@run_here
def load_config():
	os.chdir('..')
	with open('config.json', encoding = 'UTF-8') as config_file:
		config_data = json.load(config_file)
	return config_data

def config(**para):
	config_data = load_config()
	print(*config_data)
	#valid_para = dict(zip(*config_data))
	
	if len(para) == 0:
		return json.dumps(config_data, sort_key = True, indent = '\t')
	elif option_check(para, config_data, type_check = True):
		@run_here
		def update_config():
			#Generate changelog and update config_data
			for k, v in para.items():
				if config_data[k] != v:
					changelog = changelog + f'\n\t"{k}": {config_data[k]} -> {v}'
					config_data[k] = v
			
			#Save config_data to config.json
			os.chdir('..')
			with open('config.json', 'w', encoding = 'UTF-8') as config_file:
				json.dump(config_data, config_file, indent = '\t')
			
			return changelog
		
		

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