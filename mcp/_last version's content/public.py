import os
import inspect

def get_start_end_line(list, start, end):
	for i in range(len(list)):
		if (start in list[i]) and (' ' + start not in list[i]):
			for j in range(i, len(list)):
				if (end in list[j]) and (' ' + end not in list[j]):
					break
			break
	if i != None and j != None:
		return i, j
	else:
		print('Failed to find start or end line.\n\n')

def get_file_content(file, mode = 'r', return_type = 'list'):
	def return_content(path, mode = mode, return_type = return_type):
		with open(path, mode, encoding = 'UTF-8') as f:
			content = f.readlines()
			if return_type == 'list':
				return content
			elif return_type == 'str':
				str_content = ''
				for line in content:
					str_content = str_content + line
				
				return str_content
	
	file_list = ['game', 'strings']
	orig_path = os.getcwd()
	
	if file == 'string':
		file = 'strings'
	
	if file in file_list:
		os.chdir(os.path.dirname(__file__))
		content = return_content(f'game_content/{file}.js')
		os.chdir(orig_path)
		return content
	else:
		caller_info = str(inspect.stack()[1]).split(',')
		for line in caller_info:
			if "filename=" in line:
				caller_path = line.split('=', 1)[1].strip()[1:-1]
				caller_path = os.path.split(caller_path)[0]
				os.chdir(caller_path)
				break
		
		if file[2] == '.':
			dot_num = len(file.split('/', 1)[0])
			for i in range(1, dot_num):
				os.chdir('..')
			file = file[dot_num+1:]
		
		content = return_content(file)
		os.chdir(orig_path)
		return content