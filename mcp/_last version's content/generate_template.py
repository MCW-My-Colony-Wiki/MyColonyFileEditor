from .single_page import get_part, get_unit
from .public import get_file_content
from json import load, dump
import os

def generate_template(template_name, *target_name, title_use = 'default', image_use = 'default', desc_use = 'default', return_type = 'str'):
	'''
	En
	Incoming template_name and target_name(unlimited amount), generate template correspond of both.
	
	*Can use title_use, image_use, desc_use to adjust title, image, description's content.
	'''
	'''
	Zh-tw
	傳入template_name和不限數量的target_name，生成與兩者對應的template
	
	*可使用title_use, image_use, desc_use來自訂title, image, description的內容
	'''
	orig_path = os.getcwd()
	os.chdir(os.path.dirname(__file__))
	cap_template_name = str.capitalize(template_name)
	with open('dict/template_part.json', 'r', encoding = 'UTF-8') as tp:
		template_part_dic = load(tp)
	
	try:
		with open(f'dict/key_tkey/{cap_template_name}.json', 'r', encoding = 'UTF-8') as ktk:
			key_tkey_dic = load(ktk)
		with open(f'dict/key_type/{cap_template_name}.json', 'r', encoding = 'UTF-8') as kt:
			key_type_dic = load(kt)
	except FileNotFoundError:
		raise ValueError(f"Invalid template name '{template_name}'")
	
	part_name = template_part_dic[cap_template_name]
	part = get_part('game', part_name)
	public_tkey_dic = {'title':title_use, 'image':image_use, 'desc':desc_use}
	unit_list = list(target_name)
	template_list = []
	def value_converter(template_name, t_key, value):
		if t_key != '':
			#init
			key_type = key_type_dic[t_key]
			value = value.strip()
			if value[-1] == ',':
				value = value[:-1]
			
			if template_name == 'Infobox building':
				if value == 'null' or value == '0' or value == '[]':
					return None
				elif key_type == 'str':
					#init
					if value[0] == '"' and value[-1] == '"':
						value = value[1:-1]
					
					if 'tile_' in key:
						area.append(value)
					elif key == 'pack to':
						value = f'[[{value}]]'
				elif key_type == 'list':
					if '[' in value and ']' in value:
						value = value[1:-1]
						if '{' not in value:
							value_list = value.split(',')
							for i in range(len(value_list)):
								value_list[i] = value_list[i].strip()[1:-1]
							
							value = f'[[{value_list[0]}]]'
							for i in range(1, len(value_list)):
								element = value_list[i]
								value = f'{value}, [[{element}]]'
						elif '{' in value:
							value_list = []
							#start locate
							for i in range(len(value)):
								if value[i] == '{':
									for j in range(i, len(value)):
										if value[j] == '}':
											#locate success, split {"key":"value", "key1":"value1"} to ['"key":"value"', '"key1":"value1"']
											kvt = value[i+1:j].strip().split(',')
											compose = []
											#split "key":"value" to ['"key"', '"value"']
											for i in range(len(kvt)):
												key_vp = kvt[i].split(':')
												#turn '"key"' into 'key'
												for i in range(len(key_vp)):
													item = key_vp[i]
													if item[0] == '"' and item[-1] == '"':
														key_vp[i] = key_vp[i][1:-1]
												
												if key_vp[0] == 'resource' or key_vp[0] == 'amount':
													compose.append(key_vp[1])
													if len(compose) == 2:
														value_list.append(f'[[{compose[0]}]]×{compose[1]}')
												elif key_vp[0] == 'input' or key_vp[0] == 'output':
													compose.append(key_vp[1])
													if len(compose) == 2:
														value_list.append(f'[[{compose[0]}]]')
											break
							
							value = value_list[0]
							for i in range(1, len(value_list)):
								element = value_list[i]
								value = f'{value}, {element}'
			elif template_name == 'Infobox_civilizations':
				pass
			elif template_name == 'Infobox_planet_types':
				pass
			elif template_name == 'Infobox_resources':
				pass
			elif template_name == 'Infobox_technologies':
				pass
			elif template_name == 'Infobox_terrains':
				pass
			elif template_name == 'Infobox_vehicles':
				pass
			
			return value.strip()
	
	def array_converter(template_name, key, array):
		if key != '':
			key_type = key_type_dic[key]
	
	def define_ container
	for unit in unit_list:
		unit = get_unit(part, unit)[1:-1] #name -> data
		template = []
		template.append('{{' + template_name)
		for i in range(len(unit)):
			line = unit[i]
			if ':' in line and not line.startswith(' '*13):
				kvp = line.split(':', 1)
				key = kvp[0].strip()[1:-1]
				value = kvp[1].strip()
				t_key = key_tkey_dic[key]
				#public t_key check
				if t_key in public_tkey_dic.keys() and public_tkey_dic[t_key] != 'default':
					template.append(f' |{t_key} = {public_tkey_dic[t_key]}')
					continue
				#define t_value
				if value == '[':
					for j in range(i, len(unit)):
						if f"{' '*12}]" in unit[j]:
							break
					
					array = unit[i:j+1]
					array[0] = kvp[0].replace(kvp[0].strip(), kvp[1].lstrip())
					t_value = array_converter(template_name, t_key, array)
				else:
					if t_key.startswith('_'):
						pass #change with template_name
					else:
						t_value = value_converter(template_name, t_key, value)
				
				if t_key != '' and not t_key.startswith('_') and t_key not in public_tkey_dic.keys():
					line = f' |{t_key} = {t_value}'
					
					if template_name == 'Infobox building':
						if (t_key == 'can pass' or t_key == 'indenpendence' or t_key == 'premium required') and t_value == 'false':
							pass
						else:
							template.append(line)
					elif template_name == 'Infobox_civilizations':
						pass
					elif template_name == 'Infobox_planet_types':
						pass
					elif template_name == 'Infobox_resources':
						pass
					elif template_name == 'Infobox_technologies':
						pass
					elif template_name == 'Infobox_terrains':
						pass
					elif template_name == 'Infobox_vehicles':
						pass
		
		template.append('}}\n')
		if desc_use != 'default':
			for i in range(len(template)):
				if desc_use in template[i]:
					template.append(template[i])
					del template[i]
					break
		else:
			if template_name == 'Infobox building':
				template.append('{{#invoke:Description|building|{{PAGENAME}}}}')
			elif template_name == 'Infobox technology':
				template.append('{{#invoke:Description|tech|{{PAGENAME}}}}')
			elif template_name == 'Infobox vehicle':
				template.append('{{#invoke:Description|vehicle|{{PAGENAME}}}}')
		
		if return_type == 'str':
			str_template = ''
			for line in template:
				str_template = f'{str_template}\n{line}'
			template = str_template
			template_list.append(template)
		elif return_type == 'list':
			pass
		else:
			raise ValueError(f"return_type argument only accept 'str' or 'list', not {return_type}")
	
	os.chdir(orig_path)
	if len(template_list) == 1:
		return template_list[0]
	else:
		return template_list
