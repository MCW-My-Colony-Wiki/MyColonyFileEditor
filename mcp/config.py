import os
import json

from .tools.path import run_here

__all__ = [
	'load_config',
	'config'
]

@run_here
def load_config(paras = None):
	config_path = 'config.json'
	if not os.path.exists(config_path):
		from shutil import copyfile
		copyfile('default_config.json', 'config.json')
	
	with open('config.json', encoding = 'UTF-8') as config_file:
		config_data = json.load(config_file)

	if paras is None:
		return config_data
	if type(paras) is list:
		values = []
	
		for para in paras:
			try:
				value = config_data[para]
				values.append(value)
			except KeyError:
				print(f'Invalid para: "{para}"')
				return
		
		return values
	if paras in config_data.keys():
		return config_data[paras]

	print(f'Invalid para: "{paras}"')

def config(**paras):
	config_data = load_config()
	
	def update_config_data():
		changelog = 'change log:'
		
		for k, v in paras.items():
			#Check exists
			if k not in config_data:
				raise KeyError(f"Invalid key '{k}'")
			#Check type
			if type(v) != type(config_data[k]):
				raise TypeError(f"value of '{k}' must be {config_data[k].__class__.__name__}, not {v.__class__.__name__}")
			#Check value, if not same, update changelog and config_data
			if config_data[k] != v:
				changelog = changelog + f"\n  '{k}': {config_data[k]} -> {v}"
				config_data[k] = v
		
		if changelog == 'change log:':
			changelog = changelog + '\n  Nothing changed'
		
		return changelog
		
	@run_here
	def save_config():
		os.chdir('..')
		with open('config.json', 'w', encoding = 'UTF-8') as config_file:
			json.dump(config_data, config_file, indent = '\t')
		
	if len(paras) == 0:
		print(json.dumps(config_data, sort_keys = True, indent = '\t'))
		return
	
	changelog = update_config_data()
	
	if changelog:
		print(changelog)
	
	save_config()
