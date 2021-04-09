from json import loads
from ..path.run_here import run_here

__all__ = [
	"source_data"
]

def source_data(file):
	@run_here("...")
	def get_data():
		with open(f'source/{file}.json', 'r', encoding = 'UTF-8') as source_file:
			return loads(source_file.read())
	
	return get_data()
