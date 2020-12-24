__all__ = [
	'unit_error_info'
]

def unit_error_info(unit_type, unit_name, unit_list, options):
	unit_list_len = len(unit_list)
	cap_unit_type = unit_type.capitalize()

	if type(unit_name) != int and type(unit_name) != str:
	    print(f'Only accept int or str {unit_type} name')
	    return False
	if type(unit_name) == int and unit_name > unit_list_len:
	    print(f'{cap_unit_type} number out of range, max number: {unit_list_len}')
	    return False
	if type(unit_name) == str and unit_name not in unit_list:
	    print(f'Invalid {unit_type} name: {unit_name}\n\tValid {unit_type} list:')
    
	    for i in range(unit_list_len):
	        print(f'\t\t{i+1}.{unit_list[i]}')
    
	    return False
	
	return True
