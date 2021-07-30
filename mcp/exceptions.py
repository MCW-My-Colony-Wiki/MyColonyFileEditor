class MCPerror(Exception):
	def __init__(self) -> None:
		"""
		Base exception of mcp
		"""
		pass

class FileError(MCPerror):
	def __init__(self) -> None:
		"""
		Class File related error
		"""
		pass

class InvalidFileChannel(FileError):
	def __init__(self, channel):
		"""
		Invalid file channel: `channel`
		"""
		self.channel = channel
	
	def __str__(self) -> str:
		return f"Invalid file channel: {self.channel}"

class InvalidFileVersion(FileError):
	def __init__(self, version) -> None:
		"""
		Invalid file version: `version`
		"""
		self.version = version
	
	def __str__(self) -> str:
		return f"Invalid file version: {self.version}"

class InvalidFile(FileError):
	def __init__(self, file) -> None:
		"""
		Invalid file: `file`
		"""
		self.file = file
		
	def __str__(self) -> str:
		return f"Invalid file: {self.file}"

class CategoryError(MCPerror):
	def __init__(self) -> None:
		"""
		Class Category related error
		"""
		pass

class InvalidCategory(CategoryError):
	def __init__(self, name) -> None:
		"""
		Invalid category: `name`
		"""
		self.name = name
	
	def __str__(self) -> str:
		return f"Invalid category: {self.name}"

class UnitError(MCPerror):
	def __init__(self) -> None:
		"""
		Class Unit related error
		"""
		pass

class InvalidUnit(UnitError):
	def __init__(self, name) -> None:
		"""
		Invalid unit: `name`
		"""
		self.name = name
	
	def __str__(self) -> str:
		return f"Invalid unit: {self.name}"

class CacheError(MCPerror):
	def __init__(self) -> None:
		"""
		Class Cache related error
		"""
		pass

class InvalidTimeout(CacheError):
	def __init__(self, timeout) -> None:
		"""
		Invalid timeout: `timeout`, did someone change it?
		"""
		self.timeout = timeout
	
	def __str__(self) -> str:
		return f"Invalid timeout: {self.timeout}, did someone change it?"

class CacheTimeout(CacheError):
	def __init__(self) -> None:
		"""
		This cache is timeout, please update or delete it
		"""
		pass
	
	def __str__(self) -> str:
		return "This cache is timeout, please update or delete it"
