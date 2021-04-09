from ..operate.source import getcat
from ..source import ListUnit
from ..exceptions import raise_TpE

__all__ = [
	'unit_init_generater'
]

def unit_attr_analyzer(source, category):
	cat = getcat(source, category)
	
	if type(cat.data) is ListUnit:
		#sorted() -> Avoid errors caused by different element positions
		#tuple() -> Let keys(list) hashable
		#set() -> Eliminate duplicate keys
		keys_set = set(tuple(sorted(unit.keys)) for unit in cat)
		
		if len(keys_set) > 1:
			keys_list = list(keys_set)
			may_missing = [key for keys_set in [set(keys_list[i]) ^ set(keys_list[i + 1]) for i in range(len(keys_list) - 1)] for key in keys_set]
			all_attr = []
			
			#Generate all_attr that not content key in may_missing
			for unit in cat:
				for key in unit.keys:
					if key not in all_attr and key not in may_missing:
						all_attr.append(key)
			
			#Add may_missing key into all_attr, with correct position
			for unit in cat:
				for i in range(len(unit.keys) - 1):
					key = unit.keys[i]
					
					if key in may_missing and key not in all_attr:
						#Get previous key of current key
						#Get position of previous key in all_attr
						position = all_attr.index(unit.keys[i - 1]) + 1
						all_attr.insert(position, key)
			
			return all_attr, may_missing
		return cat[0].keys
	raise_TpE('category.data', ListUnit)

def unit_init_generater(source, category):
	unit_attrs = unit_attr_analyzer(source, category)
	
	if type(unit_attrs) is tuple:
		all_attr = unit_attrs[0]
		may_missing = unit_attrs[1]
		init_settings = [f"\n		self.{attr} = self.data['{attr}']" if attr not in may_missing else f"\n		self.{attr} = self.data['{attr}'] if '{attr}' in self.data else None" for attr in all_attr]
	else:
		init_settings = [f"\n		self.{attr} = self.data['{attr}']" for attr in unit_attrs]
	
	init_settings = str().join(setting for setting in init_settings)[1:]
	
	return init_settings
