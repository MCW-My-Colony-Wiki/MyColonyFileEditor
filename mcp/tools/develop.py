from ..operate.source import getcat
from ..source import ListUnit
from ..exceptions import raise_TpE

__all__ = [
	'unit_init_generater'
]

def unit_attr_analyzer(source, category):
	cat = getcat(source, category)
	
	if type(cat.data) is ListUnit:
		keys_tuple_set = set([tuple(unit.data.keys()) for unit in cat])
		
		#create all_attr, sort it at the same time
		all_attr = []
		
		for keys_tuple in keys_tuple_set:
			for key in keys_tuple:
				if key not in all_attr:
					all_attr.append(key)
		
		#generate may_missing if needed it
		keys_set_list = [set(keys_tuple) for keys_tuple in keys_tuple_set]
		keys_set_list_len = len(keys_set_list)
		
		if keys_set_list_len > 1:
			may_missing = []
			
			for i in range(keys_set_list_len - 1):
				may_missing.append(*(keys_set_list[i] ^ keys_set_list[i + 1]))
			
			may_missing = list(set(may_missing))
		
		if 'may_missing' in dir():
			return all_attr, may_missing
		return all_attr
	
	raise_TpE('category.data', ListUnit)

def unit_init_generater(source, category):
	unit_attrs = unit_attr_analyzer(source, category)
	init_settings = ''
	
	if type(unit_attrs) is tuple:
		all_attr = unit_attrs[0]
		may_missing = unit_attrs[1]
		init_setting_list = [f"\n		self.{attr} = self.data['{attr}']" if attr not in may_missing else f"\n		self.{attr} = self.data['{attr}'] if '{attr}' in self.data else None" for attr in all_attr]
	else:
		init_setting_list = [f"\n		self.{attr} = self.data['{attr}']" for attr in unit_attrs]
	
	for init_setting in init_setting_list:
		init_settings = init_settings + init_setting
	
	return init_settings.strip()
