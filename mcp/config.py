import os
import json

from .tools.path import run_here
from .tools.data import class_name

__all__ = [
	'load_config',
	'config'
]

def load_config(paras = None):
	def file_check():
		config_path = 'config.json'
		
		if not os.path.exists(config_path):
			from shutil import copyfile
			copyfile('default_config.json', 'config.json')
	
	def load():
		with open('config.json', encoding = 'UTF-8') as config_file:
			config_data = json.load(config_file)
		
		return config_data
	
	def get_value(key):
		try:
			return config_data[key]
		except KeyError:
			raise ValueError(f"Invalid para: {key}")
	
	with run_here(file_check):
		pass
	
	with run_here(load) as data:
		config_data = data
	
	if paras is None:
		return config_data
	if type(paras) is str:
		return get_value(paras)
	if type(paras) is list or type(paras) is tuple:
		values = []
		
		for para in paras:
			values.append(get_value(para))
		
		return values
	
	raise TypeError(f"the paras must be list, tuple or str, not {class_name(paras)}")

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
