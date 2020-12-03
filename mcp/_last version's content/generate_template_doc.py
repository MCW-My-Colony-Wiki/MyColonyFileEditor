from .public import get_file_content
from .category_page import get_desc

def generate_template_doc(template_name):
	template_name = str.capitalize(template_name)
	html = get_file_content(f'.../Template/{template_name.replace(" ", "_")}.html')
	source_list = []
	template = []
	article_table = []
	
	for line in html:
		if ' source=' in line:
			source = line.split(' source=')[1][1:-3]
			desc = get_desc('template', f'{source.replace(" ", "-")}-desc', template_name = template_name)
			
			source_list.append(source)
			template.append(f' |{source} = ')
			article_table.append(f''' |{source}
 |{desc}
 |-''')
	
	template.insert(0, f'''Blank full template
<pre>
{"{{"+template_name}''')
	template.append('''}}
</pre>
''')
	article_table.insert(0, '''{| class = "article-table"
 !Key
 !Description
 |-''')
	article_table[-1] = article_table[-1][:-4] + '\n|}'
	page = template + article_table
	page.append(f'''<includeonly>
  [[Category:Template|{{PAGENAME}}]]
</includeonly>

<noinclude>
  [[Category:Template documentation|{{PAGENAME}}]]
</noinclude>''')
	return page