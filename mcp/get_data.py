import json

from . import core
from .part import Part

run_here = core.run_here

def get_part(file, part):
	try:
		run_here.start()
		with open(f'cache/data/{file}_{part}.json') as part_file:
			part_data = json.loads(part_file)
		run_here.end()
		
		part = Part()