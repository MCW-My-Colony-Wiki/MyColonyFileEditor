import json
import importlib

from os.path import exists

from .tools.path.run_here import run_here
from .tools.info.class_name import class_name

__all__ = [
	'load_config',
	'config'
]

copyfile = importlib.import_module('shutil').copyfile
config_file_path = 'config.json'
default_config_file_path = 'default_config.json'

@run_here
def config_file_check():
	'''

	if config.json not exists, generate it

	'''
	if not exists(config_file_path):
		copyfile('default_config.json', 'config.json')

def load_config(*paras):
	@run_here
	def load():
		with open('config.json', encoding = 'UTF-8') as config_file:
			return json.load(config_file)
	
	config_data = load()
	
	if not paras:
		return config_data
	if len(paras) == 1:
		return config_data[paras[0]]
	return [config_data[para] for para in paras]

def config(**paras):
	config_data = load_config()
	
	def update_config_data(config_data):
		changes = 'changes'
		#all_checks = {"check_name": check_by_default}
		all_checks = {"type_check": True, "value_check": True}
		
		#customize check
		valid_value = {
			'update_from': ['stable', 'latest']
		}
		
		def check_type():
			if type(v) != type(config_data[k]):
				raise TypeError(f"value of '{k}' must be '{class_name(config_data[k])}', not '{class_name(v)}'")
		
		def check_value():
			if k in valid_value and v not in valid_value[k]:
				raise ValueError(f"Invalid value '{v}' of '{k}'\n  valid value: {str(valid_value[k])[1:-1]}")
		
		#auto generate
		set_check = {check: paras.get(check, all_checks[check]) for check in all_checks}
		local = locals()
		check_to_func = {check: local[f"check_{check.split('_')[0]}"] for check in all_checks}
		need_check = [check_to_func[k] for k, v in set_check.items() if v]

		#update config data
		def update_config_data(changes, config_data):
			if v != config_data[k]:
				changes += f"\n  '{k}': {config_data[k]} -> {v}"
				config_data[k] = v
			
			return changes, config_data
		
		#update config
		if need_check:
			for k, v in paras.items():
				for check in need_check:
					check()
				changes, config_data = update_config_data(changes, config_data)
		else:
			for k, v in paras.items():
				changes, config_data = update_config_data(changes, config_data)
		
		if changes == 'changes':
			changes += '\n  Nothing changed'
		
		return config_data, changes
		
	@run_here
	def save_config(config_data):
		with open(config_file_path, 'w', encoding = 'UTF-8') as config_file:
			json.dump(config_data, config_file, indent = '\t')
		
	if not paras:
		return json.dumps(config_data, indent = '    ')
	
	config_data, changes = update_config_data(config_data)
	
	print(changes)
	
	save_config(config_data)

config_file_check()