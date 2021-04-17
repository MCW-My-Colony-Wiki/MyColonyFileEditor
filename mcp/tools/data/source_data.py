from json import loads
from ..path.run_here import run_here

__all__ = [
	"load_source_data"
]

@run_here("...")
def read_source_file(file):
	with open(f'source/{file}.json', 'r', encoding = 'UTF-8') as source_file:
		return source_file.read()

def load_source_data(file):
	return loads(read_source_file(file))
