import os
import inspect

__all__ = [
	'run_here',
	'rela_chdir'
]

def run_here(func):
	def get_outer_func_path(frame):
		func_path = os.path.split(
			inspect.getframeinfo(
				frame.f_back
			).filename
		)[0]
		
		return func_path
	
	#Get orig_path of outermost run_here_func
	orig_path = os.getcwd()
	
	#Get func_path and allow use at module __main__
	if func.__module__ != '__main__':
		func_path = get_outer_func_path(inspect.currentframe())
	else:
		func_path = orig_path
	
	def run_here_func(*args):
		#Move to the location of the function
		os.chdir(func_path)
		
		#Get function return value
		func_return = func(*args)
		
		#Restore work directory
		outer_func = inspect.currentframe().f_back.f_back
		outer_func_info = inspect.getframeinfo(outer_func)
		
		if outer_func_info.function != 'run_here_func':
			os.chdir(orig_path)
		else:
			os.chdir(get_outer_func_path(outer_func))
		
		return func_return
	return run_here_func

def rela_chdir(path):
	'''
	path:
		Type: PathLike
	'''
	#For '../path' or '..'
	if path.startswith('..'):
		#For '../path'
		if '/' in path:
			path = path.split('/', 1)
		
			while len(path[0])-1:
				path[0] = path[0][1:]
				os.chdir('..')
			
			os.chdir(path[1])
		#For '..'
		else:
			while len(path)-1:
				os.chdir('..')
				path = path[1:]
	#Normal path
	else:
		os.chdir(path)