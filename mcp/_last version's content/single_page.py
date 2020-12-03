from .public import get_file_content, get_start_end_line

def get_part(file, part = 'all'):
	file_list = ['game', 'string', 'strings']
	
	class Setting():
		def __init__(self, space, part, asw, aew, psw, pew):
			self.space = space
			self.part = part
			self.asw = asw
			self.aew = aew
			self.psw = psw
			self.pew = pew
	
	if file in file_list:
		content = get_file_content(file)
		part_list = get_part_list(file)
		
		if file == 'strings' or file == 'string':
			setting = Setting(8, part, ' '*8 + '"', ' '*4 + '}', ' '*8 + f'"{part}"', ' '*8 + '}')
		elif file == 'game':
			setting = Setting(4, part, ' '*4 + '"', '}', ' '*4 + f'"{part}"', ' '*4 + ']')
			setting.bpl = get_part_list(file, 'braces')
		
		if setting.part == 'all':
			start_end_line = get_start_end_line(content, setting.asw, setting.aew)
		elif setting.part in part_list:
			if file == 'game' and setting.part in setting.bpl:
				start_end_line = get_start_end_line(content, setting.psw, ' '*4 + '}')
			elif setting.part in part_list:
				start_end_line = get_start_end_line(content, setting.psw, setting.pew)
		else:
			print(f'{setting.part} not in {part_list} or != "all"\n')
		
		return content[start_end_line[0]:start_end_line[1]+1]
	else:
		print(f'{file} not in {file_list}\n')

def get_part_list(file, type = 'all', keyword = ''):
	def add():
		part_name = line.strip()
		part_list.append(part_name[1:-4])
	
	file_list = ['game', 'string', 'strings']
	
	if file in file_list:
		content = get_file_content(file)
		part_list = []
		
		if file == 'game':
			space = 4
		elif file == 'string' or file == 'strings':
			space = 8
		
		if type == 'all':
			for line in content:
				if (' '*space in line) and (' '*(space+1) not in line) and (']' not in line) and ('}' not in line):
					add()
		elif type == 'braces':
			for line in content:
				if (' '*4 in line) and (' '*5 not in line) and ('{' in line):
					add()
		elif type == 'square':
			for line in content:
				if (' '*4 in line) and (' '*5 not in line) and ('[' in line):
					add()
		elif keyword != '':
			for line in content:
				if (keyword in line) and (' ' + keyword not in line):
					add()
		else:
			part_list = ['']
			print(f'{keyword} not a vaild value of keyword')
		
		return part_list
	else:
		print(f'Invaild file "{file}"')

def get_unit(part, name = 'all'):
	if (isinstance(part, list) == True) and (name != 'all'):
		for i in range(len(part)):
			if (' '*8 + '{' in part[i]) and (' '*9 + '{' not in part[i]) and (name in part[i+1]):
				for j in range(i, len(part)):
					if (' '*8 + '}' in part[j]) and (' '*9 + '}' not in part[j]):
						return part[i:j+1]
						break
				break
	else:
		unit_list = get_unit_list(part)
		content = get_part('game', part)[1:-2]
		
		if part == 'flagParts' or part == 'flagLogos':
			return content[name].strip()[1:-2]
		elif name == 'all':
			return content
		elif name in unit_list:
			start_end_line = get_start_end_line(content, ' '*8 + '{', ' '*8 + '}')
			content = content[start_end_line[0]:start_end_line[1]+1]
			return content

def get_unit_list(part):
	square_part_list = get_part_list('game', 'square')
	
	if part in square_part_list:
		content = get_part('game', part)
		unit_name = []
		
		for i in range(len(content)):
			line = content[i]
			
			if (' '*8 + '{' in line) and (' '*9 not in line):
				name = content[i+1].split(':')[1].strip()[1:-2]
				unit_name.append(name)
			
			if i == 1 and '{' not in line:
				content = content[1:-2]
				
				for j in range(len(content)):
					content[j] = content[j].strip()[1:-2]
				
				unit_name = content
				break
			
			if i != 1:
				unit_name.sort()
		
		return unit_name
	
	else:
		print(f'{part} not a vaild value of part')

