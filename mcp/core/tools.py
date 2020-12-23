import os
import re
import inspect

__all__ = [
	'run_here',
	'converter',
	'fill_dic'
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

def converter(data):
	data = re.sub(r', *//.*', ',', data) #Remove comment
	data = re.sub(r': *\.', ': 0.', data) #Remove float-like(.1, .2, ...)
	data = data.strip() #Remove space at start and end
	list_data = data.split('\n') #Prepare for get first line and last line
	while '"' not in list_data[1]:
		data = data[len(list_data[0]):-len(list_data[-1])].strip() #Remove first line and last line
		list_data = data.split('\n') #Overwrite list_data with new data
	
	data = data.replace(list_data[0], '{') #Let first line turn into "{"
	data = data.replace(list_data[-1], '}') #Let last line turn into "}"
	
	return data

def fill_dic(from_dic, to_dic, *, except_key = None):
	if len(from_dic) != len(to_dic): #Check if the two lengths are the same
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
