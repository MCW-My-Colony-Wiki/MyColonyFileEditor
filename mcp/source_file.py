from .tools.data.source_data import load_source_data

__all__ = [
	"source_files"
	"source_data"
]

source_files = [
    'game',
    'strings'
]

#Pre-created source data
source_data = {name: load_source_data(name) for name in source_files}
