from . import core
from . import data
from . import check
from .part import Part

__all__ = [
	'get_part_list',
	'get_part',
	'get_parts'
]

run_here = core.run_here()
fill_dic = core.fill_dic

def get_part_list(file_name, **options):
	'''
	If file_name is invalid, return None
	Else, return part_list
	
	options:
		check_file(Type: bool, Default: True): If True, will check file before try to get part list
	'''
	valid_option = {'check_file': True}
	
	if not check.option_check(options, valid_option):
		return
	
	options = fill_dic(valid_option, options)
	
	if options['check_file'] and not check.file_check(file_name):
		return
	
	part_list = getattr(data, file_name).parts
	
	return part_list

def get_part(file_name, part_name, **options):
	'''
	If part_name is invalid, return None
	Else, return Part
	
	options:
		check_file(Type: bool, Default: True): If True, will check file_name before try to get part
		check_part(Type: bool, Default: True): If True, will check part_name before try to get part
	'''
	import json
	
	valid_option = {'check_file': True, 'check_part': True}
	
	#Basic check
	if not check.option_check(options, valid_option):
		return
	
	#Filling options
	options = fill_dic(valid_option, options)
	
	#Optional check
	if options['check_file'] and not check.file_check(file_name):
		return
	
	part_list = get_part_list(file_name)# move for avoid use get_part_list twice
	
	if options['check_part'] and not check.part_check(file_name, part_name, check_file = False, part_list = part_list):
		return
	
	#Support use int instead part's name
	if type(part_name) == int:
		part_name = part_list[part_name - 1]
	
	#Get part_data
	try: #Get from cache
		run_here.start()
		with open(f'cache/data/{file_name}_{part_name}.json', encoding = 'UTF-8') as part_file:
			part_data = json.load(part_file)
		run_here.end()
	except FileNotFoundError: #Get from file.data and create cache
		file = getattr(data, file_name)
		part_data = file.data[part_name]
		
		run_here.start()
		with open(f'cache/data/{file_name}_{part_name}.json', 'w', encoding = 'UTF-8') as part_file:
			json.dump(part_data, part_file, indent = '\t', ensure_ascii = False)
		run_here.end()
	
	#create Part
	part = Part(file_name, part_name, part_data)
	
	return part

def get_parts(file, part_names: list, **options):
	'''
	get_part's advance version, can return mulit part at once
	'''
	part_list = []
	
	for part_name in part_names:
		part = get_part(file, part_name, options)
		
		if part == None:
			return

		part_list.append(part)
	
	if len(part_list) == 1:
		return part_list[0]
	else:
		return part_list
