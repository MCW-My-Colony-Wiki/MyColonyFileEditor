class UnitBase():
	def __init__(self, category, data, name=None) -> None:
		self.category = category
		self.data = data
		self.name = name
	
	def __str__(self) -> str:
		return str(self.data) if self.name is None else self.name
