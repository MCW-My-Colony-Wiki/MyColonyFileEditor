import json

from .core import run_here, option_check

@run_here
def load_config():
	with open('config.json', encoding = 'UTF-8') as config_file:
		config_data = json.load(config_file)
	return config_data

def config(**items):
	config_data = load_config()
	
	@run_here
	def update_config():
		for key in items.keys():
			if config_data[key] != items[key]:
				config_data[key] = items[key]
		
		with open('config.json', 'w') as config_file:
			json.dump(config_data, config_file, indent = '\t')
	
	if len(items.keys()) == 0: #Return sorted config_data
		return json.dumps(config_data, sort_keys = True, indent = '\t')
	elif option_check(items, config_data, type_check = True):
		#Generate change list
		update_content = ''
		for k, v in items.items():
			if config_data[k] != v:
				update_content = update_content + f'\n\t"{k}": {config_data[k]} -> {v}'
		
		update_config()
		
		#If change list != None, print it
		#Else, print message
		if update_content != '':
			print(f'Success update config file{update_content}')
		else:
			print('These settings are already what you want, so no settings are changed')
	else:
		return False
