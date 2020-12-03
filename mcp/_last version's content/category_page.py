from .single_page import get_part
from .public import get_file_content

def category_content(category_name):
  
def get_desc(type, desc_key, template_name = '', lang = 'en'):
	def search(list):
		for line in list:
			line = line.lstrip().split(':', 1)
			if desc_key == line[0]:
				return line[1].strip()
	
	if type == 'template' and template_name != '':
		try:
			content = get_file_content(f'template/desc/{template_name}.txt')
			return search(content)
		except FileNotFoundError:
			print(f'Invaild template name "{template_name}"')
	elif type == 'template' and template_name == '':
		print('Please input a template name')
	elif type == 'string' or type == 'strings':
		part = get_part('string', lang)
		return search(part)
	else:
		print(f'Invaild type "{type}"')