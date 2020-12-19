from . import get_part
from . import get_unit

from .core import fill_dic

__all__ = [
	'file_check',
	'option_check',
	'part_check',
	'unit_check'
]

def file_check(file_name):
	'''
	If file_name doesn't conform to the format, return False
	Else, return valid file_name
	'''
	file_list = ['game', 'strings']
	
	#Error information
	if type(file_name) != str:
		print('Only accept str file name')
		return False
	elif file_name not in file_list:
		print(f'Invalid file name: {file_name}')
		return False
	
	return True

def option_check(option, valid_option, **options):
	'''
	option: option to check
	valid_option: valid option's key-value pair, key is option's name, value is option's type
	
	options:
		type_check(Type: bool, Default: True): If true, it also checks the type
	
	*Support len(option) < len(valid_option)
	'''
	self_valid_option = {'type_check': True}
	
	def check(option, valid_option, **options):
		option_keys = list(option.keys())
		valid_option_keys = list(valid_option.keys())
		
		def exist_check(option_name):
			if option_name not in valid_option_keys:
				print(f'Invalid option: {option_name}')
				return False
		
		def type_check(option_name):
			if type(option[option_name]) != type(valid_option[option_name]):
				print(f'Incorrect option value type:\n\tOption: {option_name}\n\tInput option value type: {option[option_name].__class__.__name__}\n\tAccept option value type: {valid_option[option_name].__class__.__name__}')
				return False
		
		def do_check(check_list):
			for option_name in option_keys:
				for check in check_list:
					check_result = check(option_name)
					
					if check_result == False:
						return False
		
		options = fill_dic(self_valid_option, options)
		
		if options['type_check'] == False:
			check_result = do_check([exist_check])
		else:
			check_result = do_check([exist_check, type_check])
		
		if check_result == False:
			return False
		
		return True
	
	#Self check
	if not check(options, self_valid_option):
		return False
	
	return check(option, valid_option, **options)

def unit_error_info(unit_type, unit_name, unit_list, options):
	unit_list_len = len(unit_list)
	cap_unit_type = unit_type.capitalize()
	
	if type(unit_name) != int and type(unit_name) != str:
		print(f'Only accept int or str {unit_type} name')
		return False
	elif type(unit_name) == int and unit_name > unit_list_len:
		print(f'{cap_unit_type} number out of range, max number: {unit_list_len}')
		return False
	elif type(unit_name) == str and unit_name not in unit_list:
		print(f'Invalid {unit_type} name: {unit_name}\n\tValid {unit_type} list:')
		
		for i in range(unit_list_len):
			print(f'\t\t{i+1}.{unit_list[i]}')
		
		return False
	
	return True

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
		part_list = get_data.get_part_list(file_name)
		
		if part_list == None:
			return False
	else:
		part_list = options['part_list']
	
	if not unit_error_info('part', part_name, part_list, options):
		return False
	
	return True

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
	unit_list = get_unit.get_unit_list(file_name, part_name)
	
	if unit_list == None:
		return False
	
	if not unit_error_info('unit', unit_name, unit_list, options):
		return False
	
	return True

class check():
	pass