import json

from . import core
from .check import option_check

run_here = core.run_here()

def _load_config():
	run_here.start()
	
	with open('config.json', encoding = 'UTF-8') as config_file:
		config = json.load(config_file)
	
	run_here.end()
	return config

def config(**items):
	run_here.start()
	
	with open('config.json', encoding = 'UTF-8') as config_file:
		config_data = json.load(config_file)
	
	run_here.end()
	
	check_result = option_check(items, config_data, type_check = True)
	
	def update_config_data():
		for key in items.keys():
			if config_data[key] != items[key]:
				config_data[key] = items[key]
		
		run_here.start()
		
		with open('config.json', 'w') as config_file:
			json.dump(config_data, config_file, indent = '\t')
		
		run_here.end()
	
	if len(items.keys()) == 0:
		return json.dumps(config_data, sort_keys = True, indent = '\t')
	elif check_result == True:
		update_content = str()
		for k, v in items.items():
			if config_data[k] != v:
				update_content = update_content + f'\t"{k}": {config_data[k]} >>> {v}\n'
		update_config_data()
		
		if update_content != '':
			print(f'Success update config file\n{update_content}')
		else:
			print('These settings are already what you want, so no settings are changed')
	else:
		return False
