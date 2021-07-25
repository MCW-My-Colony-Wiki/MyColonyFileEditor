from pathlib import Path
from .libs.cache import FileCache
from .libs.request import get_channel_version, get_valid_version, get_source
from .libs.source import Source

class File():
	def __init__(self, file: str, source_channel = "stable", create_cache = True, *, source_version: str = None) -> None:
		self.version = source_version if source_version and source_version in get_valid_version() else get_channel_version(source_channel)
		cache_folder_path = Path(__file__).parent / "cache" / "source" / self.version
		cache = FileCache(cache_folder_path, file)
		
		try:
			self.data = cache.get()
			self.dict = cache.json()
		except FileNotFoundError:
			source = Source(get_source(self.version, file))
			self.data = source.data
			self.dict = source.dict
			
			if create_cache:
				cache.create(self.data, timeout=None)
		
		self.categories = list(self.dict.keys())
	
	def __getitem__(self, key):
		if key in self.categories:
			return self.categories[key]
	
	def __iter__(self):
		num = 0
		
		while num < len(self.categories):
			yield self.categories[num]
			num += 1

class Game(File):
	def __init__(self, source_channel = "stable", create_cache = True, *, source_version = None) -> None:
		super().__init__("game", source_channel=source_channel, source_version=source_version, create_cache=create_cache)

class Strings(File):
	def __init__(self, source_channel = "stable", create_cache = True, *, source_version = None) -> None:
		super().__init__("strings", source_channel=source_channel, source_version=source_version, create_cache=create_cache)
