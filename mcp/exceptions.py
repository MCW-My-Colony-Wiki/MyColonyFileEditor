class MCPerror(Exception):
	pass

class FileError(MCPerror):
	pass
class InvalidVersionChannel(FileError):
	def __str__(self, channel) -> str:
		return f"Invalid update channel `{channel}`"

class InvalidVersion(FileError):
	def __str__(self, version) -> str:
		return f"Invalid version `{version}`"

class InvalidFile(FileError):
	def __str__(self, file) -> str:
		return f"Invalid file `{file}`"
class CacheError(MCPerror):
	pass
class InvalidTimeout(CacheError):
	def __str__(self, timeout) -> str:
		return f"Invalid timeout `{timeout}`, maybe someone change it?"

class CacheTimeout(CacheError):
	def __str__(self) -> str:
		return "This cache is timeout, please update"
