from .category import DictCategory, ListCategory
from .exceptions import InvalidCategoryName
from .filebase import FileBase


__all__ = [
	"Game",
	"Strings"
]

type_to_Category = {
	dict: DictCategory,
	list: ListCategory
}

class Game(FileBase):
	def __init__(self, channel = "stable", cache = True, *, version = None) -> None:
		super().__init__("game", channel=channel, cache=cache, version=version)
	
	def __getitem__(self, name):
		try:
			category_data = self.dict[name]
			return type_to_Category[type(category_data)](self, name, category_data)
		except KeyError:
			raise InvalidCategoryName(name)

class Strings(FileBase):
	def __init__(self, channel = "stable", cache = True, *, version = None) -> None:
		super().__init__("strings", channel=channel, cache=cache, version=version)
	
	def __getitem__(self, name):
		try:
			category_data = self.dict[name]
			return DictCategory(self, name, category_data)
		except KeyError:
			raise InvalidCategoryName(name)
