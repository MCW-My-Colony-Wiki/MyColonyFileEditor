import os
import inspect
import re

__all__ = [
	'run_here',
	'converter',
	'fill_dic'
]

class run_here():
	def __init__(self):
		self.orig_path = None
	
	def start(self, position = 1):
		self.orig_path = os.getcwd()
		caller_path = os.path.split(inspect.stack()[position].filename)[0]
		os.chdir(caller_path)
	
	def end(self):
		os.chdir(self.orig_path)
		self.orig_path = None
	
	def path(self, path):
		self.orig_path = os.getcwd()
		os.chdir(path)
	
	def run_here(self, func):
		def run_here_func():
			self.start(2)
			func()
			self.end()
		return run_here_func

def converter(path):
	with open(path, 'r', encoding = 'UTF-8') as game_file:
		data = re.sub(r', *//.*', ',', game_file.read()) #Remove comment
		data = re.sub(r': *\.', ': 0.', data) #Remove float-like(.1, .2, ...)
		data = data.strip() #Remove space at start and end
		list_data = data.split('\n') #Prepare for get first line and last line
		while '"' not in list_data[1]:
			data = data[len(list_data[0]):-len(list_data[-1])].strip() #Remove first line and last line
			list_data = data.split('\n') #Overwrite list_data with new data
		
		data = data.replace(list_data[0], '{') #Let first line turn into "{"
		data = data.replace(list_data[len(list_data)-1], '}') #Let last line turn into "}"
	
	return data

def fill_dic(from_dic, to_dic, *, except_key = None):
	if len(from_dic) != len(to_dic):
		def in_dic(k, from_dic, to_dic):
			if k not in to_dic:
				to_dic[k] = from_dic[k]
		
		if except_key != None:
			for k in from_dic:
				if k not in except_key:
					in_dic(k, from_dic, to_dic)
		else:
			for k in from_dic:
				in_dic(k, from_dic, to_dic)
	
	return to_dic
