from .option_check import *
from .error_message import unit_error_info
from ..tools import fill_dic
from ..operate.part import get_part_list

def part_check(file_name, part_name, **options):
	'''
	If file_name or part_name doesn't conform to the format, return False
	Else, return True
	
	options:
		check_file(Type: bool, Default: True): If True, will check file before try to check part
		part_list(Type: list, Default: get_part_list(file_name)): If have set this option, will check weather part_name is in this part_list
			*If have set this option, will overwrite check_file to False
	'''
	valid_option = {'check_file': True, 'part_list': []}
	
	#Basic check
	if not option_check(options, valid_option):
		return False
	
	#Filling options
	options = fill_dic(valid_option, options)
	
	#Optional check
	if options['check_file'] and options['part_list'] != [] and not file_check(file_name):
		return False
	
	#Get data's information
	if options['part_list'] == []:
		part_list = get_part_list(file_name)
		
		if part_list is None:
			return False
	else:
		part_list = options['part_list']
	
	if not unit_error_info('part', part_name, part_list, options):
		return False
	
	return True