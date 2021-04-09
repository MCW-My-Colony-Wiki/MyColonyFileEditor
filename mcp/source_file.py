from .tools.data.source_data import source_data

__all__ = [
    "source_files",
    "raw_source_data"
]

source_files = [
	'game',
	'strings'
]

#Pre-created source data
raw_source_data = {name: source_data(name) for name in source_files}
