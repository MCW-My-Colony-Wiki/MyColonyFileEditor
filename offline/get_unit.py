from . import core
from . import data
from . import check

from .get_part import get_part

__all__ = [
	'get_unit_list',
	'get_unit',
	'get_units'
]

run_here = core.run_here()
fill_dic = core.fill_dic

def get_unit_list(file_name, part_name, **options):
	'''
	Base on get_part
	Basically same as get_part_list, but need give part_name and it return unit_list
	'''
	#Basic check
	valid_option = {'check_file': True, 'check_part': True}
	
	if not check.option_check(ptions, valid_option):
		return
	
	#Filling options
	options = fill_dic(valid_option, options)
	
	#Try get unit list
	try:
		unit_list = get_part(file_name, part_name, **options).units
	except AttributeError: #If get_part return None, return
		return
	
	return unit_list

def get_unit(file_name, part_name, unit_name, **options):
	'''
	
	'''
	import json
	
	valid_option = {'check_file': True, 'check_part': True, 'check_unit': True}
	
	#Basic check
	if not check.option_check(options, valid_option):
		return
	
	#Filling options and get value
	options = fill_dic(valid_option, options)
	check_file = options['check_file']
	check_part = options['check_part']
	check_unit = options['check_unit']
	
	#Optional check
	if (check_file and not check.file_check(file_name)) or (check_part and not check.part_check(file_name, part_name, check_file = False)):
		return
	
	unit_list = get_unit_list(file_name, part_name)
	
	if check_unit and not check.unit_check(file_name, part_name, unit_name, check_file = False, check_part = False):
		return
	
	#Support use int instead unit's name
	if type(unit_name) == int:
		unit_name = unit_list[unit_name - 1]
	
	try:
		run_here.start()
		with open(f'', encoding = 'UTF-8') as unit_file:
			

def get_units():
	pass