from ..tools import fill_dic

__all__ = [
	'option_check'
]

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
					
					if not check_result:
						return False
		
		options = fill_dic(self_valid_option, options)
		
		if not options['type_check']:
			check_result = do_check([exist_check])
		else:
			check_result = do_check([exist_check, type_check])
		
		if not check_result:
			return False
		
		return True
	
	#Self check
	if not check(options, self_valid_option):
		return False
	
	return check(option, valid_option, **options)
