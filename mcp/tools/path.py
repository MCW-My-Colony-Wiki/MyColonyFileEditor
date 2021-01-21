import os
from inspect import currentframe

__all__ = [
	'run_here',
	'rela_chdir'
]

class run_here():
	def __init__(self, func):
		if func.__class__.__name__ != "function":
			raise TypeError(f"the 'func' must be function, not '{func.__class__.__name__}'")
		
		self.func = func
		self.orig_path = os.getcwd()
		self.func_path = os.path.split(currentframe().f_back.f_globals['__file__'])[0]
	
	def __enter__(self):
		os.chdir(self.func_path)
		return self.func()
	
	def __exit__(self, exc_type, exc_value, exc_trackback):
		os.chdir(self.orig_path)

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