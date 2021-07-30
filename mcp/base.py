class CommonBase():
	def __delattr__(self, name: str) -> None:
		raise TypeError(f"can't set attributes of type '{self.__class__.__name__}'")
	
	def __str__(self):
		return self.name

class DictBase(CommonBase):
	def __contains__(self, name):
		return name in self.dict
	
	def __setitem__(self, name, data):
		self.dict[name] = data
	
	def __delitem__(self, name):
		try:
			del self.dict[name]
		except KeyError:
			raise KeyError(name)
	
	def __iter__(self):
		for key in self.dict:
			yield self[key]
	
	def __len__(self):
		return len(self.dict)
	
	def items(self):
		for key in self.dict:
			yield key, self[key]
	
	def clear(self):
		self.dict = {}
	
	def get(self, name, default=None):
		try:
			return self.dict[name]
		except KeyError:
			return default
	
	def pop(self, name, default=None):
		try:
			return self.dict.pop(name)
		except KeyError:
			return default

class ListBase(CommonBase):
	def __contains__(self, target):
		return target in self.list
	
	def __setitem__(self, target, data):
		if isinstance(target, int):
			self.list[target] = data
		elif isinstance(target, slice):
			try:
				self.list[target.start:target.stop:target.step] = data
			except TypeError:
				raise TypeError("can only assign an iterable")
	
	def __delitem__(self, target):
		if isinstance(target, int):
			try:
				del self.list[target]
			except IndexError:
				raise IndexError("list assignment index out of range")
		elif isinstance(target, slice):
			del self.list[target.start:target.stop:target.step]
	
	def __iter__(self):
		for i in range(len(self.list)):
			yield self[i]
	
	def __len__(self):
		return len(self.list)
	
	def append(self, __object):
		self.list.append(__object)
	
	def count(self, __value):
		return self.list.count(__value)
	
	def extend(self, __iterable):
		try:
			self.list.extend(__iterable)
		except TypeError:
			raise TypeError(f"'{__iterable.__class__.__name__}' object is not iterable")
	
	def index(self, __value, __start=None, __stop=None):
		return self.list.index(__value, __start, __stop)
	
	def insert(self, __index, __object):
		self.list.insert(__index, __object)
	
	def remove(self, __value):
		try:
			self.list.remove(__value)
		except ValueError:
			raise ValueError("'{__value}' not in list")
	
	def pop(self, __index):
		try:
			self.list.pop(__index)
		except IndexError:
			if len(self.list) == 0:
				raise IndexError("pop from empty list")
			raise IndexError("pop index out of range")
	
	def clear(self):
		self.list.clear()
	
	def sort(self, *args, key=None, reverse=False):
		self.list.sort(*args, key=key, reverse=reverse)
	
	def reverse(self):
		self.list.reverse()
