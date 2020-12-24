import os
import inspect

__all__ = [
	'run_here',
	'rel_chdir'
]

def run_here(func):
	orig_path = os.getcwd()
	func_frame = inspect.currentframe().f_back
	func_frame_info = inspect.getframeinfo(func_frame)
	func_path = os.path.split(func_frame_info.filename)[0]
	
	def run_here_func(*args):
		os.chdir(func_path) #Move to the location of the function
		func_return = func(*args) #Get function return value
		os.chdir(orig_path) #Restore work directory
		return func_return #Return function's return value
	return run_here_func #Same as above

def rel_chdir(dire):
	'''
	dire:
		Type: PathLike
		Format: f'{several_full_stop}/{path}'
	'''
	if dire.startswith('..'):
		dire = dire.split('/', 1)
		
		while len(dire[0])-1:
			dire[0] = dire[0][1:]
			os.chdir('..')
		
		os.chdir(dire[1])