__all__ = [
	'file_check'
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
	if file_name not in file_list:
	    print(f'Invalid file name: {file_name}')
	    return False
	
	return True
