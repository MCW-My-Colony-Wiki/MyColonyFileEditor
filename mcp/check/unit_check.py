from .option_check import *
from .error_message import unit_error_info
from ..tools import fill_dic
from ..operate.unit import get_unit_list

def unit_check(file_name, part_name, unit_name, **options):
	'''
	'''
	valid_option = {'check_file': True, 'check_part': True}
	
	#Basic check
	if not option_check(options, valid_option):
		return False
	
	#Filling options
	options = fill_dic(valid_option, options)
	
	#Optional check
	if options['check_file'] and not file_check(file_name):
		return False
	
	if options['check_part'] and not part_check(file_name, part_name, check_file = False):
		return False
	
	#Get unit list
	unit_list = get_unit_list(file_name, part_name)
	
	if unit_list is None:
		return False
	
	if not unit_error_info('unit', unit_name, unit_list, options):
		return False
	
	return True
