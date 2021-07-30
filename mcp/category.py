from .base import DictBase, ListBase
from .categorybase import CategoryBase
from .exceptions import InvalidUnit
from .unit import (BoolUnit, DictUnit, FloatUnit, IntUnit, ListUnit, NoneUnit,
                	StrUnit)

type_to_unit = {
	dict: DictUnit,
	list: ListUnit,
	str: StrUnit,
	int: IntUnit,
	float: FloatUnit,
	bool: BoolUnit,
	type(None): NoneUnit
}

class DictCategory(DictBase, CategoryBase):
	def __init__(self, file, name: str, data: dict) -> None:
		if type(data) is not dict:
			raise TypeError("DictCategory data must be dictionary, "
							f"not {data.__class__.__name__}")
		
		self.dict = data
		super().__init__(file, name)
	
	def __getitem__(self, name):
		try:
			unit_data = self.dict[name]
			return type_to_unit[type(unit_data)](self, unit_data, name)
		except KeyError:
			raise InvalidUnit(name)
	
	def units(self):
		return [*self.dict.keys()]

class ListCategory(ListBase, CategoryBase):
	def __init__(self, file, name, data) -> None:
		if type(data) is not list:
			raise TypeError("ListCategory data must be list, "
							f"not {data.__class__.__name__}")
		
		self.list = data
		super().__init__(file, name)
	
	def __getitem__(self, target):
		if isinstance(target, int):
			try:
				unit_data = self.list[target]
				return type_to_unit[type(unit_data)](self, unit_data)
			except IndexError:
				raise IndexError("category index out of range")
		if isinstance(target, slice):
			return self.list[target.start:target.stop:target.step]
		raise TypeError("category indices must be integers or slices, "
						f"not {target.__class__.__name__}")
	
	def units(self):
		return self.list
